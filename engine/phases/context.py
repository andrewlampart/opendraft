#!/usr/bin/env python3
"""
ABOUTME: DraftContext dataclass — mutable shared state for inter-phase communication
ABOUTME: Each phase reads inputs from ctx and writes outputs back to ctx
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class DraftContext:
    """
    Mutable inter-phase communication bus for draft generation.

    Each phase function takes a DraftContext, reads its inputs,
    and writes its outputs back onto the same object.
    """

    # ------------------------------------------------------------------
    # User inputs (set once at initialization)
    # ------------------------------------------------------------------
    topic: str = ""
    language: str = "en"
    academic_level: str = "master"
    output_type: str = "full"  # 'full' or 'expose'
    citation_style: str = "apa"  # 'apa', 'ieee', or 'nalt'
    skip_validation: bool = True
    verbose: bool = True
    blurb: Optional[str] = None

    research_goal: str = ""
    hypotheses: List[str] = field(default_factory=list)
    research_questions: List[str] = field(default_factory=list)
    research_notes: Optional[str] = None

    toc_template: str = "default"
    thesis_work_mode: str = "literature_review"
    toc_options: Dict[str, Any] = field(default_factory=dict)
    user_results_markdown: Optional[str] = None
    toc_spec: Any = None

    # Empirical uploads (paths copied into job output dir by Django task)
    survey_pdf_path: Optional[Path] = None
    empirical_dataset_path: Optional[Path] = None
    survey_questionnaire_text: str = ""
    empirical_analysis_plan_yaml: str = ""
    empirical_results_json: str = ""
    empirical_results_markdown: str = ""
    methodology_fact_sheet: str = ""

    # Academic metadata (optional, for cover page)
    author_name: Optional[str] = None
    institution: Optional[str] = None
    department: Optional[str] = None
    faculty: Optional[str] = None
    advisor: Optional[str] = None
    second_examiner: Optional[str] = None
    location: Optional[str] = None
    student_id: Optional[str] = None

    # ------------------------------------------------------------------
    # Infrastructure (set during initialization)
    # ------------------------------------------------------------------
    config: Any = None  # AppConfig instance
    model: Any = None  # GenerativeModel instance
    folders: Dict[str, Path] = field(default_factory=dict)
    word_targets: Dict[str, Any] = field(default_factory=dict)
    language_name: str = ""
    language_instruction: str = ""

    # Progress reporting (optional)
    tracker: Any = None  # ProgressTracker
    streamer: Any = None  # MilestoneStreamer

    # ------------------------------------------------------------------
    # Research phase outputs
    # ------------------------------------------------------------------
    scout_result: Optional[Dict[str, Any]] = None
    scout_output: str = ""
    scribe_output: str = ""
    signal_output: str = ""

    # ------------------------------------------------------------------
    # Structure phase outputs
    # ------------------------------------------------------------------
    architect_output: str = ""
    formatter_output: str = ""

    # ------------------------------------------------------------------
    # Citation management outputs
    # ------------------------------------------------------------------
    citation_database: Any = None  # CitationDatabase
    citation_summary: str = ""

    # ------------------------------------------------------------------
    # Compose phase outputs
    # ------------------------------------------------------------------
    intro_output: str = ""
    lit_review_output: str = ""
    methodology_output: str = ""
    results_output: str = ""
    discussion_output: str = ""
    body_output: str = ""
    conclusion_output: str = ""
    appendix_output: str = ""

    # ------------------------------------------------------------------
    # Token tracking (optional)
    # ------------------------------------------------------------------
    token_tracker: Any = None  # TokenTracker


def research_design_prompt_block(ctx: DraftContext) -> str:
    """Tekst do outline (structure) i compose — cel, hipotezy, pytania, uwagi."""
    chunks = []
    goal = (ctx.research_goal or "").strip()
    if goal:
        chunks.append(f"**Research goal:**\n{goal}")
    hyps = [h.strip() for h in (ctx.hypotheses or []) if h and str(h).strip()]
    if hyps:
        lines = "\n".join(f"{i + 1}. {h}" for i, h in enumerate(hyps))
        chunks.append(f"**Hypotheses:**\n{lines}")
    rqs = [q.strip() for q in (ctx.research_questions or []) if q and str(q).strip()]
    if rqs:
        lines = "\n".join(f"{i + 1}. {q}" for i, q in enumerate(rqs))
        chunks.append(f"**Research questions:**\n{lines}")
    notes = (ctx.research_notes or "").strip()
    if notes:
        chunks.append(f"**Additional author guidance:**\n{notes}")
    return "\n\n".join(chunks) if chunks else ""
