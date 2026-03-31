#!/usr/bin/env python3
"""
ABOUTME: Safe execution wrapper for empirical analysis scripts (AST allowlist)
ABOUTME: Prefer Docker (no network, RO data); fallback subprocess + rlimit / timeout
"""

from __future__ import annotations

import ast
import csv
import json
import re
import logging
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FuturesTimeout
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

logger = logging.getLogger(__name__)


def _sandbox_mode() -> str:
    return os.environ.get("OPENDRAFT_SANDBOX_MODE", "auto").strip().lower()


def _sandbox_image() -> str:
    return os.environ.get(
        "OPENDRAFT_SANDBOX_IMAGE", "opendraft-analysis-sandbox:latest"
    ).strip()


def _nano_cpus() -> int:
    raw = os.environ.get("OPENDRAFT_SANDBOX_CPUS", "1").strip()
    try:
        cpus = max(0.25, min(8.0, float(raw)))
    except ValueError:
        cpus = 1.0
    return int(cpus * 1_000_000_000)


def _docker_client_available() -> bool:
    try:
        import docker

        docker.from_env().ping()
        return True
    except Exception:
        return False


def _use_docker_executor() -> Tuple[bool, str]:
    """
    Returns (use_docker, error_message_if_mandatory_docker_failed).
    error set only when OPENDRAFT_SANDBOX_MODE=docker and Docker is unusable.
    """
    mode = _sandbox_mode()
    if mode == "subprocess":
        return False, ""
    if mode == "docker":
        if not _docker_client_available():
            return False, "OPENDRAFT_SANDBOX_MODE=docker, lecz Docker daemon jest niedostępny."
        return True, ""
    # auto: domyślnie subprocess (np. Railway bez gniazda Docker). Docker po jawnej zgodze.
    opt = os.environ.get("OPENDRAFT_USE_DOCKER_SANDBOX", "").strip().lower()
    if opt not in ("1", "true", "yes"):
        return False, ""
    if not _docker_client_available():
        logger.warning(
            "OpenDraft: OPENDRAFT_USE_DOCKER_SANDBOX=1, lecz Docker niedostępny — subprocess."
        )
        return False, ""
    return True, ""


def _pids_limit() -> int:
    raw = os.environ.get("OPENDRAFT_SANDBOX_PIDS_LIMIT", "256").strip()
    try:
        return max(64, min(2048, int(raw)))
    except ValueError:
        return 256


def _docker_run_user() -> Optional[str]:
    """
    Nadpisanie użytkownika w kontenerze, np. "1001:1001" gdy worker Celery ma inny UID
    niż domyślne 1000 z obrazu. Puste = domyślny USER z Dockerfile.
    """
    u = os.environ.get("OPENDRAFT_SANDBOX_CONTAINER_USER", "").strip()
    return u or None


def _run_analysis_docker(
    *,
    workdir: Path,
    data_csv: Path,
    timeout_sec: int,
) -> Tuple[bool, str, Optional[Dict[str, Any]]]:
    import docker
    from docker.errors import ImageNotFound

    image = _sandbox_image()
    client = docker.from_env()
    workdir = Path(workdir).resolve()
    data_csv = Path(data_csv).resolve()
    result_path = workdir / "results.json"

    volumes = {
        str(workdir): {"bind": "/work", "mode": "rw"},
        str(data_csv): {"bind": "/input/dataset.csv", "mode": "ro"},
    }
    environment = {
        "OPENDRAFT_DATA_CSV": "/input/dataset.csv",
        "OPENDRAFT_RESULT_JSON": "/work/results.json",
        "PYTHONUNBUFFERED": "1",
    }

    try:
        client.images.get(image)
    except ImageNotFound:
        return (
            False,
            f"Obraz sandboxa nie istnieje lokalnie: {image}. "
            f"Zbuduj: docker build -t {image} -f opendraft/docker/analysis_sandbox/Dockerfile .",
            None,
        )

    run_kw: Dict[str, Any] = dict(
        image=image,
        command=["python3", "/work/run_analysis.py"],
        volumes=volumes,
        environment=environment,
        network_mode="none",
        mem_limit=f"{_sandbox_max_mem_mb()}m",
        nano_cpus=_nano_cpus(),
        pids_limit=_pids_limit(),
        read_only=True,
        tmpfs={"/tmp": "rw,nosuid,size=128m"},
        security_opt=["no-new-privileges:true"],
        working_dir="/work",
    )
    du = _docker_run_user()
    if du:
        run_kw["user"] = du
    container = client.containers.create(**run_kw)
    try:
        container.start()
        with ThreadPoolExecutor(max_workers=1) as pool:
            fut = pool.submit(container.wait)
            try:
                fut.result(timeout=timeout_sec)
            except FuturesTimeout:
                try:
                    container.kill()
                except Exception:
                    pass
                try:
                    fut.result(timeout=15)
                except Exception:
                    pass
                return False, f"Timeout after {timeout_sec}s", None

        container.reload()
        exit_code = container.attrs.get("State", {}).get("ExitCode")
        log_txt = ""
        try:
            raw = container.logs(stdout=True, stderr=True)
            log_txt = raw.decode("utf-8", errors="replace") if raw else ""
        except Exception as e:
            log_txt = f"(logs unavailable: {e})"

        if exit_code != 0:
            return False, (log_txt or f"exit {exit_code}")[:8000], None
    finally:
        try:
            container.remove(force=True)
        except Exception:
            pass

    if not result_path.is_file():
        return False, "Script did not write results.json", None
    try:
        data = json.loads(result_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON in results.json: {e}", None
    return True, "", data


# Production subprocess limits (Unix only; Windows uses timeout only).
def _sandbox_max_mem_mb() -> int:
    raw = os.environ.get("OPENDRAFT_SANDBOX_MAX_MEM_MB", "512").strip()
    try:
        return max(64, min(4096, int(raw)))
    except ValueError:
        return 512


def _sandbox_cpu_sec() -> int:
    raw = os.environ.get("OPENDRAFT_SANDBOX_CPU_SEC", "60").strip()
    try:
        return max(5, min(600, int(raw)))
    except ValueError:
        return 60


def _sandbox_preexec() -> None:
    """Child process: cap virtual memory and CPU time (Linux/macOS)."""
    if sys.platform == "win32":
        return
    try:
        import resource

        mem_bytes = _sandbox_max_mem_mb() * 1024 * 1024
        cpu_soft = _sandbox_cpu_sec()
        # RLIMIT_AS: virtual address space (Linux); may not limit RSS on all OSes.
        try:
            resource.setrlimit(resource.RLIMIT_AS, (mem_bytes, mem_bytes))
        except (ValueError, OSError) as e:
            logger.debug("RLIMIT_AS not applied: %s", e)
        try:
            resource.setrlimit(
                resource.RLIMIT_CPU, (cpu_soft, cpu_soft + 5)
            )
        except (ValueError, OSError) as e:
            logger.debug("RLIMIT_CPU not applied: %s", e)
    except ImportError:
        pass

ALLOWED_TOP_LEVEL_MODULES: Set[str] = {
    "json",
    "math",
    "statistics",
    "pathlib",
    "csv",
    "re",
    "datetime",
    "collections",
    "itertools",
    "functools",
    "typing",
    "os",
    "pandas",
    "pd",
    "numpy",
    "np",
    "scipy",
    "scipy.stats",
    "matplotlib",
    "matplotlib.pyplot",
}

FORBIDDEN_NAMES: Set[str] = {
    "exec",
    "eval",
    "__import__",
    "compile",
    "open",  # scripts must use Path.read/write only via pathlib or we inject
    "input",
    "breakpoint",
    # os module dangerous methods
    "system",
    "popen",
    "execv",
    "execve",
    "execvp",
    "execvpe",
    "spawnl",
    "spawnle",
    "spawnlp",
    "spawnlpe",
    "spawnv",
    "spawnve",
    "spawnvp",
    "spawnvpe",
    "fork",
    "forkpty",
    "posix_spawn",
    # other dangerous builtins/attrs
    "globals",
    "locals",
    "vars",
    "getattr",
    "setattr",
    "delattr",
}


def _collect_imports(tree: ast.AST) -> Tuple[Set[str], Optional[str]]:
    """Return top-level module roots used; error message if disallowed."""
    roots: Set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                roots.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                roots.add(node.module.split(".")[0])
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in FORBIDDEN_NAMES:
                return roots, f"Forbidden call: {node.func.id}"
    for r in roots:
        if r not in ALLOWED_TOP_LEVEL_MODULES and not r.startswith("_"):
            if r in ("scipy", "numpy", "pandas"):
                continue
            return roots, f"Disallowed import root: {r}"
    return roots, None


def validate_analysis_script(source: str) -> Tuple[bool, str]:
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        return False, f"SyntaxError: {e}"
    _, err = _collect_imports(tree)
    if err:
        return False, err
    dump = ast.dump(tree)
    for bad in ("subprocess", "socket", "shutil.rmtree", "os.system", "pty."):
        if bad in dump:
            return False, f"Forbidden construct: {bad}"
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute):
            if node.attr in FORBIDDEN_NAMES:
                return False, f"Forbidden attribute: {node.attr}"
    return True, ""


_DATE_PATTERNS = (
    re.compile(r"^\d{4}-\d{2}-\d{2}"),
    re.compile(r"^\d{2}[./-]\d{2}[./-]\d{4}"),
    re.compile(r"^\d{2}[./-]\d{2}[./-]\d{2}$"),
)


def _infer_column_type_from_samples(values: List[str]) -> str:
    """Infer numeric / categorical / date / unknown from header sample cells (no pandas)."""
    non_empty = [str(v).strip() for v in values if v is not None and str(v).strip() != ""]
    if not non_empty:
        return "unknown"
    numeric_ok = 0
    date_ok = 0
    n = len(non_empty)
    for v in non_empty:
        vs = v.replace(",", ".").replace(" ", "")
        try:
            float(vs)
            numeric_ok += 1
        except ValueError:
            pass
        if any(p.match(v) for p in _DATE_PATTERNS):
            date_ok += 1
    if numeric_ok >= max(1, int(0.8 * n)):
        return "numeric"
    if date_ok >= max(1, int(0.8 * n)):
        return "date"
    return "categorical"


def profile_csv(path: Path, *, sample_rows: int = 5) -> Dict[str, Any]:
    """Lightweight CSV profile without pandas (stdlib)."""
    path = Path(path)
    out: Dict[str, Any] = {
        "path": str(path),
        "columns": [],
        "sample_rows": [],
        "column_types": {},
        "row_count_estimate": 0,
        "error": "",
    }
    if not path.is_file():
        out["error"] = "not a file"
        return out
    try:
        with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            if not header:
                out["error"] = "empty csv"
                return out
            cols = [c.strip() for c in header]
            out["columns"] = cols
            rows: List[List[str]] = []
            n = 0
            for row in reader:
                n += 1
                if len(rows) < sample_rows:
                    rows.append(row[: len(cols)])
            out["sample_rows"] = rows
            out["row_count_estimate"] = n
            col_types: Dict[str, str] = {}
            for i, col in enumerate(cols):
                col_vals = [row[i] if i < len(row) else "" for row in rows]
                col_types[col] = _infer_column_type_from_samples(col_vals)
            out["column_types"] = col_types
    except Exception as e:
        out["error"] = str(e)
    return out


def ensure_csv_dataset(path: Path, workdir: Path) -> Path:
    """
    If path is Excel, convert to CSV in workdir via pandas; else return path.
    """
    path = Path(path)
    suffix = path.suffix.lower()
    if suffix in (".xlsx", ".xls"):
        try:
            import pandas as pd

            df = pd.read_excel(path)
            dest = workdir / "dataset_normalized.csv"
            df.to_csv(dest, index=False, encoding="utf-8")
            return dest
        except Exception as e:
            logger.warning("Excel→CSV failed, using original: %s", e)
    return path


def _run_analysis_subprocess(
    *,
    script_path: Path,
    workdir: Path,
    result_path: Path,
    data_csv: Path,
    timeout_sec: int,
) -> Tuple[bool, str, Optional[Dict[str, Any]]]:
    env = os.environ.copy()
    env["OPENDRAFT_DATA_CSV"] = str(Path(data_csv).resolve())
    env["OPENDRAFT_RESULT_JSON"] = str(result_path.resolve())

    try:
        if sys.platform != "win32":
            proc = subprocess.run(
                [sys.executable, str(script_path)],
                cwd=str(workdir),
                env=env,
                capture_output=True,
                text=True,
                timeout=timeout_sec,
                preexec_fn=_sandbox_preexec,
            )
        else:
            proc = subprocess.run(
                [sys.executable, str(script_path)],
                cwd=str(workdir),
                env=env,
                capture_output=True,
                text=True,
                timeout=timeout_sec,
            )
    except subprocess.TimeoutExpired:
        return False, f"Timeout after {timeout_sec}s", None

    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "")[:8000]
        return False, err, None

    if not result_path.is_file():
        return False, "Script did not write results.json", None

    try:
        data = json.loads(result_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON in results.json: {e}", None

    return True, "", data


def run_analysis_script(
    script_source: str,
    *,
    data_csv: Path,
    workdir: Path,
    timeout_sec: int = 120,
) -> Tuple[bool, str, Optional[Dict[str, Any]]]:
    """
    Write script to workdir, run with OPENDRAFT_DATA_CSV / OPENDRAFT_RESULT_JSON.

    Production: set OPENDRAFT_SANDBOX_MODE=docker (or auto + OPENDRAFT_SANDBOX_IMAGE)
    and mount Docker socket; dataset mounted read-only inside the container.
    """
    data_csv = Path(data_csv)
    logger.info(
        "Sandbox: data_csv=%s exists=%s size=%s mode=%s",
        data_csv,
        data_csv.is_file(),
        data_csv.stat().st_size if data_csv.is_file() else "N/A",
        _sandbox_mode(),
    )

    ok, msg = validate_analysis_script(script_source)
    if not ok:
        logger.warning("Sandbox AST validation FAILED: %s", msg)
        return False, f"[AST validation] {msg}", None

    logger.info("Sandbox AST validation OK")

    workdir = Path(workdir)
    workdir.mkdir(parents=True, exist_ok=True)
    script_path = workdir / "run_analysis.py"
    result_path = workdir / "results.json"
    if result_path.exists():
        result_path.unlink()

    script_path.write_text(script_source, encoding="utf-8")
    logger.info("Sandbox: script written to %s (%d chars)", script_path, len(script_source))

    use_docker, docker_err = _use_docker_executor()
    logger.info("Sandbox executor: use_docker=%s docker_err=%r", use_docker, docker_err)
    if _sandbox_mode() == "docker" and docker_err:
        return False, docker_err, None

    if use_docker:
        logger.info("Sandbox: launching Docker executor")
        return _run_analysis_docker(
            workdir=workdir,
            data_csv=data_csv,
            timeout_sec=timeout_sec,
        )

    logger.info("Sandbox: launching subprocess executor (timeout=%ds)", timeout_sec)
    ok2, err2, data2 = _run_analysis_subprocess(
        script_path=script_path,
        workdir=workdir,
        result_path=result_path,
        data_csv=data_csv,
        timeout_sec=timeout_sec,
    )
    if ok2:
        logger.info("Sandbox subprocess OK, result keys=%s", list(data2.keys()) if data2 else None)
    else:
        logger.warning("Sandbox subprocess FAILED:\n%s", err2[:4000])
    return ok2, err2, data2
