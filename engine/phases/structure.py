#!/usr/bin/env python3
"""
ABOUTME: Structure phase — Architect and Formatter agents
ABOUTME: Creates thesis outline and applies academic formatting
"""

import logging

from .context import DraftContext

logger = logging.getLogger(__name__)


def run_structure_phase(ctx: DraftContext) -> None:
    """
    Execute the structure phase: Architect -> Formatter.

    Mutates ctx: architect_output, formatter_output
    """
    from utils.agent_runner import run_agent, rate_limit_delay
    from utils.document_labels import document_type_for_outline
    from utils.thesis_toc_templates import formatter_user_input_suffix

    if ctx.verbose:
        print("\n🏗\ufe0f  PHASE 2: STRUCTURE")

    if ctx.tracker:
        ctx.tracker.log_activity(
            "📋 Designing thesis structure", event_type="milestone", phase="structure"
        )
        ctx.tracker.update_phase(
            "structure", progress_percent=25, details={"stage": "creating_outline"}
        )
        ctx.tracker.check_cancellation()

    # -----------------------------------------------------------------------
    # AGENT: Architect
    # -----------------------------------------------------------------------
    if ctx.tracker:
        ctx.tracker.log_activity(
            "🏗\ufe0f Creating thesis outline...", event_type="info", phase="structure"
        )

    total_words = ctx.word_targets["total"]
    chapters_info = ctx.word_targets["chapters"]

    doc_type = document_type_for_outline(ctx.academic_level, ctx.language)

    outline_context = f"Create draft outline for: {ctx.topic}"
    if ctx.blurb:
        outline_context += f"\n\nFocus/Context: {ctx.blurb}"
    outline_context += (
        f"\n\nResearch gaps:\n{ctx.signal_output[:2000]}\n\n"
        f"Length: {total_words} words (document type: {doc_type}, {chapters_info} chapters)"
    )

    spec = getattr(ctx, "toc_spec", None)
    if spec is not None and spec.template_id != "default":
        outline_context += (
            "\n\n**MANDATORY TABLE-OF-CONTENTS TEMPLATE** — keep every section from the skeleton; "
            "only replace text in [square brackets] with titles suited to the topic. "
            "Do not merge or drop chapters.\n"
        )
        outline_context += formatter_user_input_suffix(spec, ctx.language)
    outline_context += (
        f"\n\n**Work mode for writing phase:** {ctx.thesis_work_mode} "
        f"(literature_review = synthesize prior research; empirical = thesis structured around own study design)."
    )

    ctx.architect_output = run_agent(
        model=ctx.model,
        name="Architect - Design Structure",
        prompt_path="prompts/02_structure/architect.md",
        user_input=outline_context,
        save_to=ctx.folders["drafts"] / "00_outline.md",
        skip_validation=ctx.skip_validation,
        verbose=ctx.verbose,
        token_tracker=ctx.token_tracker,
        token_stage="architect",
    )

    if ctx.tracker:
        ctx.tracker.log_activity(
            "\u2705 Outline created", event_type="found", phase="structure"
        )

    rate_limit_delay()

    # -----------------------------------------------------------------------
    # AGENT: Formatter
    # -----------------------------------------------------------------------
    formatter_extra = ""
    if spec is not None and spec.template_id != "default":
        formatter_extra = formatter_user_input_suffix(spec, ctx.language)
    opts = ctx.toc_options if isinstance(ctx.toc_options, dict) else {}
    formatter_user = (
        f"Apply academic formatting:\n\n{ctx.architect_output[:2500]}{formatter_extra}\n\n"
        f"Style: APA 7th edition\n\n"
        f"TOC options: numbering={opts.get('numbering', 'roman_arabic')}, "
        f"include_abbreviations={opts.get('include_abbreviations', False)}, "
        f"include_annex={opts.get('include_annex', True)}."
    )

    ctx.formatter_output = run_agent(
        model=ctx.model,
        name="Formatter - Apply Style",
        prompt_path="prompts/02_structure/formatter.md",
        user_input=formatter_user,
        save_to=ctx.folders["drafts"] / "00_formatted_outline.md",
        skip_validation=ctx.skip_validation,
        verbose=ctx.verbose,
        token_tracker=ctx.token_tracker,
        token_stage="formatter",
    )

    # MILESTONE: Outline Complete - Stream to user
    if ctx.streamer:
        chapters_count = ctx.formatter_output.count(
            "## Chapter"
        ) + ctx.formatter_output.count("# Chapter")
        ctx.streamer.stream_outline_complete(
            outline_path=ctx.folders["drafts"] / "00_formatted_outline.md",
            chapters_count=chapters_count if chapters_count > 0 else 5,
        )

    if ctx.tracker:
        ctx.tracker.update_phase(
            "structure",
            progress_percent=30,
            details={"stage": "outline_complete", "milestone": "outline_complete"},
        )

    rate_limit_delay()
