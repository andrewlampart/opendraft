#!/usr/bin/env python3
"""
ABOUTME: One-page methodology + results fact sheet for cross-chapter consistency
ABOUTME: Injected into Discussion / Conclusion prompts
"""

from __future__ import annotations

import logging
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from phases.context import DraftContext

logger = logging.getLogger(__name__)


def build_methodology_fact_sheet(ctx: "DraftContext") -> str:
    """
    Summarize frozen facts from methodology + results + empirical JSON for downstream writers.
    """
    from .text_utils import clean_agent_output

    meth = (ctx.methodology_output or "")[:6000]
    res = (ctx.results_output or "")[:6000]
    emp = (ctx.empirical_results_json or "")[:4000]
    rd = []
    if ctx.research_goal:
        rd.append(f"Goal: {ctx.research_goal[:800]}")
    if ctx.hypotheses:
        rd.append(
            "Hypotheses: "
            + "; ".join(h[:200] for h in ctx.hypotheses[:6] if h)
        )
    if ctx.research_questions:
        rd.append(
            "Research questions: "
            + "; ".join(q[:200] for q in ctx.research_questions[:6] if q)
        )
    research = "\n".join(rd)

    system = (
        "You are an academic editor. Produce a dense FACT SHEET (max 400 words) "
        "listing only concrete, checkable claims: sample/design, instruments, "
        "statistical procedures, and numeric outcomes. Use bullet points. "
        "If empirical JSON is present, every number in the fact sheet must come from it or "
        "from the Results excerpt. Output in the draft language implied by the excerpts."
    )
    user = f"""Topic: {ctx.topic}

{research}

**Methodology excerpt:**
{meth}

**Results excerpt:**
{res}

**Empirical JSON (ground truth if present):**
{emp}
"""
    try:
        resp = ctx.model.generate_content(f"{system}\n\n---\n\n{user}")
        text = clean_agent_output(str(getattr(resp, "text", "") or "").strip())
        if len(text) < 80:
            return _fallback_sheet(ctx)
        return (
            "**CROSS-CHAPTER FACT SHEET (must stay consistent with this):**\n\n" + text
        )
    except Exception as e:
        logger.warning("fact_sheet LLM failed: %s", e)
        return _fallback_sheet(ctx)


def _fallback_sheet(ctx: "DraftContext") -> str:
    """Heuristic fallback without extra LLM."""
    parts = ["**CROSS-CHAPTER FACT SHEET (auto):**\n"]
    if ctx.empirical_results_markdown:
        # first 2500 chars of markdown block
        m = ctx.empirical_results_markdown[:2500]
        parts.append(m)
    if ctx.methodology_output:
        parts.append("\n**Methodology (truncated):**\n" + ctx.methodology_output[:1500])
    return "\n".join(parts)


def extract_allowed_numbers_from_empirical(ctx: "DraftContext") -> str:
    """Comma-separated numeric literals from empirical JSON for anti-fabrication hint."""
    raw = ctx.empirical_results_json or ""
    nums = re.findall(
        r"-?\d+(?:[.,]\d+)?(?:e-?\d+)?", raw, flags=re.IGNORECASE
    )
    if not nums:
        return ""
    uniq = []
    for n in nums:
        if n not in uniq:
            uniq.append(n)
        if len(uniq) >= 80:
            break
    return ", ".join(uniq)
