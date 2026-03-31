#!/usr/bin/env python3
"""
ABOUTME: Actor–critic loop for compose phase (reviewer + optional revision)
ABOUTME: Reduces generic AI prose when score below threshold
"""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import TYPE_CHECKING, Optional, Tuple

if TYPE_CHECKING:
    from phases.context import DraftContext

logger = logging.getLogger(__name__)

_MAX_ROUNDS = 3
_PASS_SCORE = 4  # 1–5 scale


def _parse_score(text: str) -> int:
    m = re.search(r"SCORE:\s*(\d)\s*/\s*5", text, re.I)
    if m:
        return max(1, min(5, int(m.group(1))))
    m2 = re.search(r"SCORE:\s*(\d)", text, re.I)
    if m2:
        return max(1, min(5, int(m2.group(1))))
    return 3


def review_section(
    ctx: "DraftContext",
    *,
    section_title: str,
    markdown: str,
) -> Tuple[int, str]:
    """
    Returns (score_1_to_5, full_review_text).
    """
    from utils.text_utils import clean_agent_output

    lang = getattr(ctx, "language_name", "English") or "English"
    system = (
        f"You are a harsh thesis examiner. Respond in {lang}.\n"
        "Evaluate the section for: (1) academic tone, (2) logical link to research goal "
        "and hypotheses, (3) concrete claims vs vague filler.\n"
        "First line MUST be exactly: SCORE: N/5 where N is 1-5.\n"
        "Then bullet list of issues and actionable fixes."
    )
    user = f"**Section:** {section_title}\n\n**Draft:**\n{markdown[:14_000]}\n"
    try:
        resp = ctx.model.generate_content(f"{system}\n\n---\n\n{user}")
        review = clean_agent_output(str(getattr(resp, "text", "") or "").strip())
        return _parse_score(review), review
    except Exception as e:
        logger.warning("review_section failed: %s", e)
        return 5, f"SCORE: 5/5\n(review skipped: {e})"


def revise_section(
    ctx: "DraftContext",
    *,
    section_title: str,
    draft: str,
    review_feedback: str,
    extra_constraints: str = "",
) -> str:
    from utils.agent_runner import run_agent

    user = f"""Revise this thesis section. Keep citations and headings structure.
Address every point from the reviewer.

**Section:** {section_title}

**Reviewer feedback:**
{review_feedback[:6000]}

**Current draft:**
{draft[:12_000]}
{extra_constraints}
"""
    return run_agent(
        model=ctx.model,
        name=f"Reviser - {section_title}",
        prompt_path="prompts/03_compose/crafter.md",
        user_input=user,
        save_to=None,
        skip_validation=True,
        verbose=False,
        token_tracker=ctx.token_tracker,
        token_stage="compose_reviser",
    )


def writer_reviewer_loop(
    ctx: "DraftContext",
    *,
    section_title: str,
    initial_markdown: str,
    save_path: Optional[Path],
    extra_constraints: str = "",
) -> str:
    """
    Up to _MAX_ROUNDS reviewer passes; revise if score < _PASS_SCORE.
    """
    from utils.agent_runner import rate_limit_delay

    tr = getattr(ctx, "tracker", None)
    if tr:
        tr.update_phase(
            "compose_review",
            progress_percent=55,
            details={
                "stage": "compose_review_start",
                "message": f"Recenzent analizuje spójność i jakość: «{section_title[:100]}»…",
            },
        )
        tr.log_activity(
            f"Recenzent (actor–critic) ocenia rozdział: {section_title[:120]}",
            event_type="info",
            phase="compose_review",
        )

    text = initial_markdown
    for round_i in range(_MAX_ROUNDS):
        score, review = review_section(ctx, section_title=section_title, markdown=text)
        logger.info(
            "compose_review %s round %s score=%s", section_title, round_i + 1, score
        )
        if tr:
            tr.log_activity(
                f"Recenzja w toku ({section_title[:50]}…) — runda {round_i + 1}, ocena {score}/5",
                event_type="info",
                phase="compose_review",
            )
        if score >= _PASS_SCORE:
            break
        if round_i + 1 >= _MAX_ROUNDS:
            break
        if tr:
            tr.log_activity(
                f"Model poprawia rozdział po uwagach recenzenta (runda {round_i + 1})…",
                event_type="writing",
                phase="compose_review",
            )
        text = revise_section(
            ctx,
            section_title=section_title,
            draft=text,
            review_feedback=review,
            extra_constraints=extra_constraints,
        )
        rate_limit_delay()
    if save_path is not None:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        Path(save_path).write_text(text, encoding="utf-8")
    return text
