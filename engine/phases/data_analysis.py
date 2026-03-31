#!/usr/bin/env python3
"""
ABOUTME: Empirical data analysis phase — YAML plan, codegen, sandbox, repair loop
ABOUTME: Runs before compose when dataset path is set (empirical jobs)
"""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Dict, Optional

from .context import DraftContext, research_design_prompt_block

logger = logging.getLogger(__name__)

_MAX_REPAIR_ROUNDS = 3


def _generate(ctx: DraftContext, system: str, user: str) -> str:
    from utils.text_utils import clean_agent_output

    full = f"{system}\n\n---\n\n{user}"
    resp = ctx.model.generate_content(full)
    text = getattr(resp, "text", None) or ""
    return clean_agent_output(str(text).strip())


def _strip_code_fence(s: str) -> str:
    s = s.strip()
    m = re.match(r"^```(?:python|yaml)?\s*\n(.*)\n```\s*$", s, re.DOTALL | re.IGNORECASE)
    if m:
        return m.group(1).strip()
    if s.startswith("```"):
        s = re.sub(r"^```\w*\s*", "", s)
        s = re.sub(r"\s*```$", "", s)
    return s.strip()


def _results_to_writer_markdown(data: Any) -> str:
    """Flatten JSON results for compose prompts (anti-fabrication)."""
    try:
        raw = json.dumps(data, ensure_ascii=False, indent=2)
    except TypeError:
        raw = str(data)
    if len(raw) > 14_000:
        raw = raw[:14_000] + "\n... [truncated] ..."
    return (
        "**EMPIRICAL ANALYSIS OUTPUT (ground truth — cite ONLY these numbers):**\n\n"
        f"```json\n{raw}\n```"
    )


def run_data_analysis_phase(ctx: DraftContext) -> None:
    """
    If empirical_dataset_path points to a file, run plan → code → execute → repair.
    Sets ctx.empirical_results_json, ctx.empirical_results_markdown, ctx.empirical_analysis_plan_yaml.
    """
    ds = ctx.empirical_dataset_path
    research = ctx.folders.get("research")
    if ds is None and research:
        inputs_dir = Path(research) / "empirical_inputs"
        if inputs_dir.is_dir():
            for pattern in ("dataset.csv", "dataset.xlsx", "dataset.xls"):
                p = inputs_dir / pattern
                if p.is_file():
                    ctx.empirical_dataset_path = p
                    ds = p
                    break
    if ds is None:
        return
    path = Path(ds)
    if not path.is_file():
        logger.info("Empirical dataset path not a file, skipping data_analysis")
        return

    if not (ctx.survey_questionnaire_text or "").strip() and research:
        sdir = Path(research) / "empirical_inputs"
        for ext in (".pdf", ".PDF"):
            sp = sdir / f"survey{ext}"
            if sp.is_file():
                from utils.pdf_extractor import extract_survey_text

                ctx.survey_questionnaire_text = extract_survey_text(sp)
                break

    if getattr(ctx, "thesis_work_mode", "") != "empirical":
        logger.info("thesis_work_mode != empirical, skipping automated data_analysis")
        return

    tr = getattr(ctx, "tracker", None)
    if tr:
        tr.update_phase(
            "data_analysis",
            progress_percent=22,
            details={
                "stage": "data_analysis_start",
                "message": "Analiza statystyczna ankiety i zbioru danych w toku…",
            },
        )
        tr.log_activity(
            "Rozpoczęto analizę danych (profil CSV, plan, sandbox)",
            event_type="info",
            phase="data_analysis",
        )

    workdir = ctx.folders["research"] / "empirical"
    workdir.mkdir(parents=True, exist_ok=True)

    from utils.data_sandbox import ensure_csv_dataset, profile_csv, run_analysis_script

    csv_path = ensure_csv_dataset(path, workdir)
    cached = workdir / "results.json"
    if cached.is_file() and csv_path.is_file():
        try:
            if cached.stat().st_mtime >= csv_path.stat().st_mtime:
                ctx.empirical_results_json = cached.read_text(encoding="utf-8")
                data = json.loads(ctx.empirical_results_json)
                ctx.empirical_results_markdown = _results_to_writer_markdown(data)
                plan_p = workdir / "analysis_plan.yaml"
                if plan_p.is_file():
                    ctx.empirical_analysis_plan_yaml = plan_p.read_text(
                        encoding="utf-8"
                    )
                logger.info("Reusing cached empirical results.json")
                if tr:
                    tr.log_activity(
                        "Wykorzono zapisane wyniki analizy",
                        event_type="milestone",
                        phase="data_analysis",
                    )
                return
        except Exception:
            pass
    profile = profile_csv(csv_path)

    if profile.get("error"):
        logger.warning("CSV profile failed: %s", profile.get("error"))
        ctx.empirical_results_markdown = (
            f"**Dataset profiling failed:** {profile.get('error')}\n"
            "Results section should describe limitations and request manual analysis."
        )
        return

    rd = research_design_prompt_block(ctx)
    survey = (ctx.survey_questionnaire_text or "").strip()
    survey_block = (
        f"\n\n**Questionnaire / survey text (from PDF):**\n{survey[:12_000]}\n"
        if survey
        else ""
    )

    col_lines = "\n".join(f"- {c}" for c in profile.get("columns", []))
    sample = json.dumps(profile.get("sample_rows", []), ensure_ascii=False)

    system_plan = (
        "You are a quantitative research methodologist. Output ONLY valid YAML "
        "(no markdown fences) describing statistical analyses to run."
    )
    user_plan = f"""Topic: {ctx.topic}

{rd}
{survey_block}

**CSV columns:**
{col_lines}

**Estimated row count:** {profile.get("row_count_estimate", "?")}

**Sample rows (first few):**
{sample}

Produce YAML with keys:
- analyses: list of objects with keys: id, description, variables (list), test_or_procedure (e.g. chi2, ttest_ind, pearsonr, descriptive), rationale
- notes: optional string

Keep analyses aligned with hypotheses / research questions. At most 8 analyses."""

    plan_yaml = _strip_code_fence(_generate(ctx, system_plan, user_plan))
    (workdir / "analysis_plan.yaml").write_text(plan_yaml, encoding="utf-8")
    ctx.empirical_analysis_plan_yaml = plan_yaml
    if tr:
        tr.log_activity(
            "Wygenerowano plan analiz statystycznych (YAML)",
            event_type="milestone",
            phase="data_analysis",
        )

    system_code = """You are a Python data analyst. Write ONE complete Python script.

Rules:
- Read the CSV path from environment variable OPENDRAFT_DATA_CSV using os.environ and pathlib.Path.
- Write a JSON-serializable dict to the path in OPENDRAFT_RESULT_JSON (use json.dump or Path.write_text).
- Use pandas (pd.read_csv). You may use numpy, scipy.stats, statistics, math, json, os, pathlib.
- Do NOT use: open() as a function name for files — use Path.read_text/write_text or pd.read_csv only.
- Do NOT use subprocess, socket, requests, or __import__.
- Handle missing values sensibly (dropna or fillna) and coerce numeric columns where needed.
- The output JSON must include key "analyses" (list of per-analysis result dicts with id, summary, statistics) and key "dataset" (row_count, columns).
- If a test cannot be run, record error in that analysis entry instead of crashing the whole script.
"""
    user_code = f"""Analysis plan (YAML):\n{plan_yaml}\n\nColumn names must match exactly: {profile.get("columns")}\n\nReturn ONLY the Python source code, no fences."""

    script = _strip_code_fence(_generate(ctx, system_code, user_code))

    last_err = ""
    for attempt in range(_MAX_REPAIR_ROUNDS):
        if tr:
            tr.log_activity(
                f"Uruchomienie skryptu analizy (próba {attempt + 1}/{_MAX_REPAIR_ROUNDS})",
                event_type="info",
                phase="data_analysis",
            )
        ok, msg, data = run_analysis_script(
            script,
            data_csv=csv_path,
            workdir=workdir,
            timeout_sec=120,
        )
        if ok and data is not None:
            ctx.empirical_results_json = json.dumps(data, ensure_ascii=False)
            ctx.empirical_results_markdown = _results_to_writer_markdown(data)
            (workdir / "results.json").write_text(
                ctx.empirical_results_json, encoding="utf-8"
            )
            logger.info("Empirical data_analysis OK (%s analyses)", attempt + 1)
            if tr:
                tr.log_activity(
                    "Analiza w sandboxie zakończona pomyślnie",
                    event_type="milestone",
                    phase="data_analysis",
                )
            return

        last_err = msg or "unknown error"
        logger.warning("data_analysis attempt %s failed: %s", attempt + 1, last_err[:500])
        repair_user = f"""The script failed. Fix it.

Error output:
```
{last_err[:6000]}
```

Previous script:
```python
{script[:12000]}
```

Return ONLY the corrected full Python script."""

        script = _strip_code_fence(
            _generate(
                ctx,
                system_code + "\nPreserve the same env vars OPENDRAFT_DATA_CSV and OPENDRAFT_RESULT_JSON.",
                repair_user,
            )
        )

    logger.error("data_analysis exhausted repairs")
    if tr:
        tr.log_activity(
            "Sandbox wyczerpał naprawy — generowanie placeholdera (LLM)",
            event_type="error",
            phase="data_analysis",
        )

    profile_summary = json.dumps(
        {
            "columns": profile.get("columns", []),
            "row_count": profile.get("row_count_estimate", 0),
            "sample": (profile.get("sample_rows") or [])[:3],
        },
        ensure_ascii=False,
    )
    lang_name = getattr(ctx, "language_name", None) or "Polish"
    fallback_md = _generate(
        ctx,
        system=(
            "You are a descriptive statistician. Based only on column names and sample rows "
            "(no computation), write a brief placeholder for the empirical Results section."
        ),
        user=(
            f"Topic: {ctx.topic}\nResearch goal: {ctx.research_goal}\n"
            f"Dataset profile: {profile_summary}\nWrite a 2-paragraph placeholder in Polish "
            f"(or {lang_name}) acknowledging that automated analysis failed."
        ),
    )
    ctx.empirical_results_markdown = (
        "**[PLACEHOLDER — analiza automatyczna nie powiodła się]**\n\n"
        + fallback_md
        + "\n\n**Uwaga:** Uzupełnij wyniki ręcznie po zakończeniu generacji.\n\n"
        "**Ostatni błąd sandboxa (skrót):**\n```text\n"
        + (last_err[:1500] or "")
        + "\n```"
    )
    ctx.empirical_results_json = json.dumps(
        {"fallback": True, "columns": profile.get("columns", []), "last_error": last_err[:2000]},
        ensure_ascii=False,
    )
