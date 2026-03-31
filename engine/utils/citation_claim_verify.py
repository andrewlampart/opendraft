#!/usr/bin/env python3
"""
ABOUTME: Claim–citation sanity check using abstracts (validate phase)
ABOUTME: Writes qa_citation_claims.md; does not auto-edit the draft
"""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, List, Tuple

if TYPE_CHECKING:
    from phases.context import DraftContext

logger = logging.getLogger(__name__)

_CITE_RE = re.compile(r"\{(cite_\d{3})\}")


def _paragraphs_with_citations(text: str, *, max_paragraphs: int = 12) -> List[Tuple[int, str]]:
    out: List[Tuple[int, str]] = []
    blocks = [p.strip() for p in text.split("\n\n") if p.strip()]
    for i, p in enumerate(blocks):
        if _CITE_RE.search(p) and len(p) > 80:
            out.append((i, p[:1200]))
        if len(out) >= max_paragraphs:
            break
    return out


def _abstracts_for_cites(
    ctx: "DraftContext", cite_ids: List[str]
) -> Dict[str, str]:
    db = getattr(ctx, "citation_database", None)
    if not db or not getattr(db, "citations", None):
        return {}
    by_id = {c.id: c for c in db.citations}
    out: Dict[str, str] = {}
    for cid in cite_ids:
        c = by_id.get(cid)
        if not c:
            continue
        ab = (getattr(c, "abstract", None) or "")[:900]
        if not ab:
            ab = (getattr(c, "title", None) or "")[:400]
        out[cid] = ab
    return out


def run_citation_claim_verification(ctx: "DraftContext") -> None:
    """
    Sample paragraphs with {{cite_*}} from literature review; LLM TRUE/FALSE per claim.
    """
    if getattr(ctx, "skip_validation", True):
        return
    lit_path = ctx.folders["drafts"] / "02_1_literature_review.md"
    if not lit_path.is_file():
        return

    text = lit_path.read_text(encoding="utf-8")
    samples = _paragraphs_with_citations(text, max_paragraphs=10)
    if not samples:
        return

    from utils.text_utils import clean_agent_output

    lines: List[str] = ["# Citation claim verification (automated)\n"]
    batch_parts: List[str] = []
    for idx, para in samples:
        cites = list(dict.fromkeys(_CITE_RE.findall(para)))
        abs_map = _abstracts_for_cites(ctx, cites)
        if not abs_map:
            continue
        abst = "\n".join(f"- {k}: {v[:500]}" for k, v in abs_map.items())
        batch_parts.append(f"### Paragraph {idx}\n{para}\n**Abstracts:**\n{abst}\n")

    if not batch_parts:
        return

    system = (
        "For each paragraph, answer whether the cited abstracts plausibly support "
        "the concrete claims in the paragraph. Reply with lines: "
        "P<idx> SUPPORTED: YES or NO — one line per paragraph. Be strict."
    )
    user = "\n\n".join(batch_parts)[:14_000]
    try:
        resp = ctx.model.generate_content(f"{system}\n\n---\n\n{user}")
        verdict = clean_agent_output(str(getattr(resp, "text", "") or "").strip())
    except Exception as e:
        logger.warning("citation claim verify LLM failed: %s", e)
        verdict = f"(verification failed: {e})"

    lines.append(verdict)
    out = ctx.folders["drafts"] / "qa_citation_claims.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    logger.info("Wrote %s", out)
