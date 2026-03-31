#!/usr/bin/env python3
"""
ABOUTME: Extract plain text from survey / questionnaire PDFs (PyMuPDF)
ABOUTME: Used for empirical pipeline — map questions to dataset columns
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, List

logger = logging.getLogger(__name__)

try:
    import fitz  # PyMuPDF

    HAS_FITZ = True
except ImportError:
    fitz = None  # type: ignore[assignment]
    HAS_FITZ = False


@dataclass
class SurveyPDFContent:
    path: str
    text: str = ""
    page_count: int = 0
    success: bool = False
    error: str = ""


class SurveyPDFExtractor:
    """Full-text extraction from a local PDF (questionnaire)."""

    def __init__(self, *, max_pages: int = 0) -> None:
        self.max_pages = max_pages

    def extract(self, path: str | Path) -> SurveyPDFContent:
        path = Path(path)
        if not HAS_FITZ:
            return SurveyPDFContent(
                path=str(path),
                error="PyMuPDF (fitz) not installed",
            )
        if not path.is_file():
            return SurveyPDFContent(path=str(path), error=f"File not found: {path}")
        try:
            with fitz.open(str(path)) as doc:
                n = doc.page_count
                limit = n if self.max_pages <= 0 else min(n, self.max_pages)
                parts: List[str] = []
                for i in range(limit):
                    parts.append(doc.load_page(i).get_text("text") or "")
                text = "\n\n".join(p.strip() for p in parts if p.strip())
            return SurveyPDFContent(
                path=str(path),
                text=text,
                page_count=n,
                success=bool(text.strip()),
            )
        except Exception as e:
            logger.exception("PDF extract failed for %s", path)
            return SurveyPDFContent(path=str(path), error=str(e))


def extract_survey_text(path: str | Path, *, max_chars: int = 24_000) -> str:
    """
    Return extracted questionnaire text for LLM prompts, truncated safely.
    """
    r = SurveyPDFExtractor().extract(path)
    if not r.success:
        if r.error:
            logger.warning("Survey PDF: %s", r.error)
        return ""
    t = r.text.strip()
    if len(t) > max_chars:
        return t[:max_chars] + "\n\n[... truncated ...]"
    return t
