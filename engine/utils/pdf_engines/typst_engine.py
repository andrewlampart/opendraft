#!/usr/bin/env python3
"""
ABOUTME: Typst PDF engine — pandoc markdown→typst, then typst compile
ABOUTME: Optional; requires `pandoc` with typst writer and `typst` CLI
"""

from __future__ import annotations

import logging
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import List

from .base import PDFEngine, PDFGenerationOptions, EngineResult

logger = logging.getLogger(__name__)


def _pandoc_supports_typst() -> bool:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        return False
    try:
        r = subprocess.run(
            [pandoc, "--list-output-formats"],
            capture_output=True,
            text=True,
            timeout=15,
        )
        return r.returncode == 0 and "typst" in (r.stdout or "").lower()
    except (OSError, subprocess.TimeoutExpired):
        return False


class TypstPDFEngine(PDFEngine):
    """Render academic PDF via Typst (pandoc as MD→Typst bridge)."""

    def get_name(self) -> str:
        return "Typst"

    def get_priority(self) -> int:
        return 90

    def is_available(self) -> bool:
        return shutil.which("typst") is not None and _pandoc_supports_typst()

    def generate(
        self, md_file: Path, output_pdf: Path, options: PDFGenerationOptions
    ) -> EngineResult:
        err = self.validate_inputs(md_file, output_pdf)
        if err:
            return EngineResult(
                success=False, engine_name=self.get_name(), error_message=err
            )

        pandoc = shutil.which("pandoc")
        typst_bin = shutil.which("typst")
        assert pandoc and typst_bin

        template_dir = Path(__file__).resolve().parent.parent.parent / "templates" / "typst"
        lang = (getattr(options, "document_language", None) or "pl").split("-")[0].lower()
        preamble_name = "preamble_en.typ" if lang == "en" else "preamble_pl.typ"
        preamble_path = template_dir / preamble_name
        if not preamble_path.is_file():
            preamble_path = template_dir / "preamble.typ"
        preamble = ""
        if preamble_path.is_file():
            preamble = preamble_path.read_text(encoding="utf-8").strip() + "\n\n"

        with tempfile.TemporaryDirectory(prefix="opendraft_typst_") as tmp:
            tdir = Path(tmp)
            body_typ = tdir / "body.typ"
            r1 = subprocess.run(
                [pandoc, str(md_file), "-s", "-t", "typst", "-o", str(body_typ)],
                capture_output=True,
                text=True,
                timeout=180,
            )
            if r1.returncode != 0:
                msg = (r1.stderr or r1.stdout or "pandoc typst failed")[:4000]
                return EngineResult(
                    success=False,
                    engine_name=self.get_name(),
                    error_message=msg,
                )

            body_text = body_typ.read_text(encoding="utf-8")
            main_typ = tdir / "main.typ"
            main_typ.write_text(preamble + body_text, encoding="utf-8")

            r2 = subprocess.run(
                [typst_bin, "compile", str(main_typ), str(output_pdf)],
                cwd=str(tdir),
                capture_output=True,
                text=True,
                timeout=240,
            )
            if r2.returncode != 0:
                msg = (r2.stderr or r2.stdout or "typst compile failed")[:4000]
                return EngineResult(
                    success=False,
                    engine_name=self.get_name(),
                    error_message=msg,
                )

        if not output_pdf.is_file():
            return EngineResult(
                success=False,
                engine_name=self.get_name(),
                error_message="typst did not produce output PDF",
            )

        warnings: List[str] = []
        if options.title:
            warnings.append("Typst template uses pandoc metadata from markdown frontmatter.")
        return EngineResult(
            success=True,
            engine_name=self.get_name(),
            output_path=output_pdf,
            warnings=warnings,
        )
