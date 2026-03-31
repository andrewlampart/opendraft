#!/usr/bin/env python3
"""
ABOUTME: Compile and export phase — assembly, abstract, PDF/DOCX export
ABOUTME: Also handles expose mode early-exit export
"""

import re
import time
import logging
import zipfile
from pathlib import Path
from typing import List, Tuple
from datetime import datetime

from .context import DraftContext

logger = logging.getLogger(__name__)


def _extract_figure_captions(md: str) -> List[str]:
    seen = set()
    out: List[str] = []
    for m in re.finditer(r"!\[([^\]]*)\]\([^)]+\)", md):
        cap = (m.group(1) or "").strip()
        if cap and cap not in seen:
            seen.add(cap)
            out.append(cap)
    return out


def _extract_table_captions(md: str) -> List[str]:
    out: List[str] = []
    seen = set()
    for line in md.splitlines():
        s = line.strip()
        if re.match(r"^:\s*(Table|Tabela)\s+", s, re.I):
            t = re.sub(r"^:\s*", "", s).strip()
            if t not in seen:
                seen.add(t)
                out.append(t)
        m = re.match(r"^\*\*((?:Table|Tabela)\s+[^*]+)\*\*\s*$", s, re.I)
        if m:
            t = m.group(1).strip()
            if t not in seen:
                seen.add(t)
                out.append(t)
    return out


def _format_lof_lot(
    figures: List[str],
    tables: List[str],
    fig_heading: str,
    tbl_heading: str,
    lang_pl: bool,
) -> str:
    parts = []
    if figures:
        parts.append("## " + fig_heading + "\n\n" + "\n".join(f"- {c}" for c in figures))
    else:
        note = (
            "*(Brak wykrytych podpisów rysunków — użyj `![Rys. N. podpis](url)` w treści.)*"
            if lang_pl
            else "*(No figure captions found — use `![Fig. N. caption](url)` in the body.)*"
        )
        parts.append("## " + fig_heading + "\n\n" + note)
    if tables:
        parts.append("## " + tbl_heading + "\n\n" + "\n".join(f"- {c}" for c in tables))
    else:
        note = (
            "*(Brak wykrytych podpisów tabel — użyj linii `: Tabela N. podpis` pod tabelą.)*"
            if lang_pl
            else "*(No table captions found — use `: Table N. caption` below each table.)*"
        )
        parts.append("## " + tbl_heading + "\n\n" + note)
    return "\n\n".join(parts)


def run_expose_export(ctx: DraftContext) -> Tuple[Path, Path]:
    """
    Handle expose mode: generate research overview + outline only.

    Returns: (pdf_path, docx_path)
    """
    from utils.export_professional import export_pdf, export_docx
    from utils.text_utils import slugify, get_language_name
    from utils.document_labels import draft_type_export_label, expose_strings

    logger.info("=" * 80)
    logger.info("EXPOSE MODE: Generating research overview (skipping full draft)")
    logger.info("=" * 80)

    if ctx.tracker:
        ctx.tracker.log_activity(
            "📋 Creating Research Expose...", event_type="milestone", phase="exporting"
        )
        ctx.tracker.update_phase(
            "exporting", progress_percent=70, details={"stage": "creating_expose"}
        )

    language_name = get_language_name(ctx.language)
    S = expose_strings(ctx.language)
    doc_type_label = draft_type_export_label(ctx.academic_level, ctx.language)

    if ctx.verbose:
        print("\n📋 EXPOSE MODE: Creating research overview...")

    # Extract research credibility info from citations
    journals = set()
    years = set()
    author_teams = []
    all_authors = set()
    source_types = {"journal": 0, "book": 0, "conference": 0, "other": 0}
    top_tier_journals = {
        "Nature",
        "Science",
        "Cell",
        "PNAS",
        "JAMA",
        "Lancet",
        "BMJ",
        "IEEE",
        "ACM",
        "Physical Review",
        "Chemical Reviews",
    }

    top_tier_count = 0
    recent_count = 0  # Last 5 years
    current_year = datetime.now().year

    for citation in ctx.citation_database.citations:
        if citation.journal:
            journals.add(citation.journal)
            # Check if top-tier
            if any(top in citation.journal for top in top_tier_journals):
                top_tier_count += 1
        if citation.year:
            years.add(citation.year)
            if current_year - citation.year <= 5:
                recent_count += 1
        if citation.authors:
            all_authors.update(citation.authors)
            lead = citation.authors[0] if citation.authors else "Unknown"
            if len(citation.authors) > 1:
                author_teams.append(f"{lead} et al.")
            else:
                author_teams.append(lead)
        # Count source types
        src_type = getattr(citation, "source_type", "journal")
        if src_type in source_types:
            source_types[src_type] += 1
        else:
            source_types["other"] += 1

    total_sources = len(ctx.citation_database.citations)
    year_range = f"{min(years)}-{max(years)}" if years else S["year_range_various"]
    top_journals = ", ".join(list(journals)[:5]) if journals else S["fallback_journals"]
    key_researchers = (
        ", ".join(author_teams[:5]) if author_teams else S["fallback_researchers"]
    )
    recency_pct = int((recent_count / total_sources) * 100) if total_sources else 0
    unique_authors = len(all_authors)

    # Compile the expose document
    n_cit = len(ctx.citation_database.citations)
    expose_content = f"""# {S["doc_heading"]}: {ctx.topic}

**{S["lbl_generated"]}:** {datetime.now().strftime('%Y-%m-%d')}
**{S["lbl_doc_type"]}:** {doc_type_label}
**{S["lbl_language"]}:** {language_name}

---

## {S["h_executive"]}

{S["p_executive"].format(topic=ctx.topic, n=n_cit)}

---

## {S["h_sources"]}

| {S["tbl_metric"]} | {S["tbl_value"]} |
|--------|-------|
| **{S["row_total"]}** | {total_sources} {S["unit_papers"]} |
| **{S["row_years"]}** | {year_range} |
| **{S["row_recent"]}** | {recency_pct}% {S["row_recent_suffix"]} |
| **{S["row_authors"]}** | {unique_authors} {S["unit_researchers"]} |
| **{S["row_toptier"]}** | {top_tier_count} |
| **{S["row_journals"]}** | {top_journals} |
| **{S["row_teams"]}** | {key_researchers} |

{S["p_sources_blurb"].format(authors=unique_authors, journals=len(journals), recency=recency_pct)}

---

## {S["h_outline"]}

{ctx.formatter_output}

---

## {S["h_findings"]}

{ctx.scribe_output[:4000] if len(ctx.scribe_output) > 4000 else ctx.scribe_output}

---

## {S["h_gaps"]}

{ctx.signal_output[:2000] if len(ctx.signal_output) > 2000 else ctx.signal_output}

---

## {S["h_bib"]}

"""
    for citation in ctx.citation_database.citations:
        authors_str = ", ".join(citation.authors[:3])
        if len(citation.authors) > 3:
            authors_str += " et al."
        expose_content += f"- {authors_str} ({citation.year}). {citation.title}"
        if citation.journal:
            expose_content += f". *{citation.journal}*"
        if citation.doi:
            expose_content += f". https://doi.org/{citation.doi}"
        expose_content += "\n\n"

    expose_content += f"""
---

## {S["h_next"]}

{S["p_next_intro"].format(doc_type=doc_type_label)}

1. **{S["next_1"]}**
2. **{S["next_2"]}**
3. **{S["next_3"]}**
4. **{S["next_4"]}**

---

{S["footer"]}
"""

    # Save expose markdown
    expose_md_path = ctx.folders["drafts"] / "00_expose.md"
    expose_md_path.write_text(expose_content, encoding="utf-8")
    logger.info(f"Expose markdown saved: {expose_md_path}")

    if ctx.tracker:
        ctx.tracker.log_activity(
            "📄 Exporting Research Expose...", event_type="info", phase="exporting"
        )
        ctx.tracker.update_phase(
            "exporting", progress_percent=85, details={"stage": "exporting_expose"}
        )

    # Export as PDF and DOCX
    topic_slug = slugify(ctx.topic, max_length=50)
    if not topic_slug:
        topic_slug = "research_expose"

    if ctx.verbose:
        print("📄 Exporting PDF...")

    pdf_path = ctx.folders["exports"] / f"{topic_slug}_expose.pdf"
    # Try 'auto' engine which falls back through multiple engines
    # For expose (quick overview), PDF is optional - don't fail if it doesn't work
    pdf_success, _pdf_err = export_pdf(
        md_file=expose_md_path, output_pdf=pdf_path, engine="auto"
    )

    if not pdf_success or not pdf_path.exists():
        logger.warning(f"PDF export failed for expose - continuing with DOCX only")
        if ctx.verbose:
            print("   ⚠️ PDF export failed (continuing with DOCX)")
        pdf_path = None  # Signal that PDF wasn't created

    if ctx.verbose:
        print("📝 Exporting Word document...")

    docx_path = ctx.folders["exports"] / f"{topic_slug}_expose.docx"
    docx_success = export_docx(md_file=expose_md_path, output_docx=docx_path)

    if not docx_success or not docx_path.exists():
        raise RuntimeError(f"DOCX export failed for expose: {docx_path}")

    if ctx.tracker:
        ctx.tracker.log_activity(
            "🎉 Research Expose complete!", event_type="milestone", phase="completed"
        )
        ctx.tracker.update_phase(
            "exporting",
            progress_percent=100,
            sources_count=len(ctx.citation_database.citations),
            chapters_count=1,
            details={"stage": "expose_complete", "milestone": "expose_complete"},
        )

    if ctx.verbose:
        print(f"\n\u2705 Research Expose complete!")
        if pdf_path:
            print(f"   PDF: {pdf_path}")
        print(f"   DOCX: {docx_path}")

    # Return paths (pdf_path may be None if PDF export failed, fall back to md)
    return pdf_path or expose_md_path, docx_path


def run_compile_and_export(ctx: DraftContext) -> Tuple[Path, Path]:
    """
    Execute the compile and export phase: assemble draft, generate abstract, export.

    Returns: (pdf_path, docx_path)
    """
    from utils.agent_runner import run_agent
    from utils.citation_compiler import CitationCompiler
    from utils.abstract_generator import generate_abstract_for_draft
    from utils.export_professional import export_pdf, export_docx
    from utils.text_utils import (
        clean_ai_language,
        strip_meta_text,
        localize_chapter_headings,
        clean_agent_output,
    )
    from utils.text_cleanup import apply_full_cleanup
    from utils.text_utils import slugify

    if ctx.verbose:
        print("\n🔧 PHASE 4: COMPILE")

    if ctx.tracker:
        ctx.tracker.log_activity(
            "🔧 Starting document compilation",
            event_type="milestone",
            phase="compiling",
        )
        ctx.tracker.update_phase(
            "compiling", progress_percent=75, details={"stage": "assembling_draft"}
        )
        ctx.tracker.check_cancellation()

    spec = getattr(ctx, "toc_spec", None)
    modern_shell = bool(spec and not spec.use_legacy_document_shell)
    lang_base = (ctx.language or "en").split("-")[0].lower()
    lang_pl = lang_base == "pl"

    # Strip headers from section outputs (modern shell keeps top-level # headings from crafters)
    if modern_shell:
        intro_clean = clean_agent_output(ctx.intro_output).strip()
        body_clean = clean_agent_output(ctx.body_output).strip()
        conclusion_clean = clean_agent_output(ctx.conclusion_output).strip()
    else:
        intro_clean = _strip_first_header(clean_agent_output(ctx.intro_output))
        body_clean = _strip_first_header(clean_agent_output(ctx.body_output))
        conclusion_clean = _strip_first_header(clean_agent_output(ctx.conclusion_output))

    appendices_file = ctx.folders["drafts"] / "04_appendices.md"
    if appendices_file.exists():
        appendix_content = appendices_file.read_text(encoding="utf-8")
        ap_raw = clean_agent_output(appendix_content)
        appendix_clean = ap_raw.strip() if modern_shell else _strip_first_header(ap_raw)
    else:
        appendix_clean = ""

    current_date = datetime.now().strftime("%B %Y")

    # Calculate word count / pages
    draft_text = f"{intro_clean}\n{body_clean}\n{conclusion_clean}\n{appendix_clean}"
    word_count = len(draft_text.split())
    pages_estimate = word_count // 250

    from utils.document_labels import draft_type_export_label, degree_export_label

    draft_type = draft_type_export_label(ctx.academic_level, ctx.language)
    degree = degree_export_label(ctx.academic_level, ctx.language)

    # YAML metadata
    yaml_author = ctx.author_name or "OpenDraft AI"
    yaml_institution = ctx.institution or "OpenDraft University"
    yaml_department = ctx.department or "Department of Computer Science"
    yaml_faculty = ctx.faculty or "Faculty of Engineering"
    yaml_advisor = ctx.advisor or "Prof. Dr. OpenDraft Supervisor"
    yaml_second_examiner = ctx.second_examiner or "Prof. Dr. Second Examiner"
    yaml_location = ctx.location or "Munich"
    yaml_student_id = ctx.student_id or "N/A"

    opts = ctx.toc_options if isinstance(ctx.toc_options, dict) else {}

    if modern_shell and spec is not None:
        ref_h = spec.references_heading_pl if lang_pl else spec.references_heading_en
        abbr_block = ""
        if opts.get("include_abbreviations"):
            ah = spec.abbreviations_heading_pl if lang_pl else spec.abbreviations_heading_en
            note = (
                "*(Wykaz do uzupełnienia w edytorze.)*"
                if lang_pl
                else "*(Complete this list in the editor.)*"
            )
            abbr_block = f"## {ah}\n\n{note}\n\n\\newpage\n\n"
        lists_block = ""
        if opts.get("include_figures_tables", True):
            joined_core = f"{intro_clean}\n{body_clean}\n{conclusion_clean}"
            fh = spec.list_figures_heading_pl if lang_pl else spec.list_figures_heading_en
            th = spec.list_tables_heading_pl if lang_pl else spec.list_tables_heading_en
            lists_block = (
                "\n\n\\newpage\n\n"
                + _format_lof_lot(
                    _extract_figure_captions(joined_core),
                    _extract_table_captions(joined_core),
                    fh,
                    th,
                    lang_pl,
                )
            )
        appendix_block = ""
        if appendix_clean.strip():
            appendix_block = f"\n\n\\newpage\n\n{appendix_clean}"
        full_draft = f"""---
title: "{ctx.topic}"
author: "{yaml_author}"
date: "{current_date}"
institution: "{yaml_institution}"
department: "{yaml_department}"
faculty: "{yaml_faculty}"
degree: "{degree}"
advisor: "{yaml_advisor}"
second_examiner: "{yaml_second_examiner}"
location: "{yaml_location}"
student_id: "{yaml_student_id}"
project_type: "{draft_type}"
word_count: "{word_count:,} words"
pages: "{pages_estimate}"
generated_by: "OpenDraft AI - https://github.com/federicodeponte/opendraft"
---

## Abstract
[Abstract will be generated]

\\newpage

{abbr_block}{intro_clean}

\\newpage

{body_clean}

\\newpage

{conclusion_clean}
{lists_block}

\\newpage

# {ref_h}
[Citations will be compiled]
{appendix_block}
"""
    else:
        full_draft = f"""---
title: "{ctx.topic}"
author: "{yaml_author}"
date: "{current_date}"
institution: "{yaml_institution}"
department: "{yaml_department}"
faculty: "{yaml_faculty}"
degree: "{degree}"
advisor: "{yaml_advisor}"
second_examiner: "{yaml_second_examiner}"
location: "{yaml_location}"
student_id: "{yaml_student_id}"
project_type: "{draft_type}"
word_count: "{word_count:,} words"
pages: "{pages_estimate}"
generated_by: "OpenDraft AI - https://github.com/federicodeponte/opendraft"
---

## Abstract
[Abstract will be generated]

\\newpage

# 1. Introduction
{intro_clean}

\\newpage

# 2. Main Body
{body_clean}

\\newpage

# 3. Conclusion
{conclusion_clean}

\\newpage

# 4. Appendices
{appendix_clean}

\\newpage

# 5. References
[Citations will be compiled]
"""

    # Citation compilation
    if ctx.tracker:
        ctx.tracker.log_activity(
            "📚 Compiling citations and references...",
            event_type="info",
            phase="compiling",
        )

    compiler = CitationCompiler(database=ctx.citation_database, model=ctx.model)
    reference_list = compiler.generate_reference_list(full_draft)
    compiled_draft, replaced_ids, failed_ids = compiler.compile_citations(
        full_draft, research_missing=True, verbose=ctx.verbose
    )

    if ctx.tracker:
        ctx.tracker.log_activity(
            f"\u2705 Citations compiled ({len(replaced_ids)} references)",
            event_type="found",
            phase="compiling",
        )

    # Remove template References section and append generated one
    compiled_draft = re.sub(
        r"^\s*#+ (?:\d+\.\s*)?(?:References|Bibliography|Bibliografia|Piśmiennictwo|Spis\s+literatury)\s*\n\s*\[Citations will be compiled\]\s*",
        "",
        compiled_draft,
        flags=re.MULTILINE | re.IGNORECASE,
    )
    compiled_draft = compiled_draft + reference_list

    # Save intermediate draft for abstract generation
    intermediate_md_path = ctx.folders["exports"] / "INTERMEDIATE_DRAFT.md"
    intermediate_md_path.write_text(compiled_draft, encoding="utf-8")

    # Generate abstract
    if ctx.tracker:
        ctx.tracker.log_activity(
            "📝 Generating abstract...", event_type="info", phase="compiling"
        )

    abstract_success, abstract_updated_content = generate_abstract_for_draft(
        draft_path=intermediate_md_path,
        model=ctx.model,
        run_agent_func=run_agent,
        output_dir=ctx.folders["exports"],
        verbose=ctx.verbose,
    )

    if ctx.tracker:
        ctx.tracker.log_activity(
            "\u2705 Abstract generated", event_type="found", phase="compiling"
        )

    final_draft = (
        abstract_updated_content
        if abstract_success and abstract_updated_content
        else compiled_draft
    )

    # Generate filename
    base_filename = slugify(ctx.topic, max_length=50)
    if not base_filename:
        base_filename = "research_paper"

    # Clean and save final markdown
    final_md_path = ctx.folders["exports"] / f"{base_filename}.md"
    final_draft = fix_single_line_tables(final_draft)
    final_draft = deduplicate_appendices(final_draft)
    final_draft = clean_malformed_markdown(final_draft)
    final_draft = clean_agent_output(final_draft)

    # Apply comprehensive text cleanup (vocab diversity, claim calibration, fillers, etc.)
    cleanup_result = apply_full_cleanup(final_draft)
    final_draft = cleanup_result["text"]
    cleanup_stats = cleanup_result["stats"]
    total_fixes = sum(cleanup_stats.values())
    logger.info(f"Text cleanup applied: {cleanup_stats}")

    if ctx.verbose and total_fixes > 0:
        print(
            f"   ✨ Text cleanup: {total_fixes} fixes (fillers={cleanup_stats['fillers']}, "
            f"vocab={cleanup_stats['vocab_diversified']}, claims={cleanup_stats['claims_calibrated']})"
        )

    if ctx.tracker and total_fixes > 0:
        ctx.tracker.log_activity(
            f"✨ Prose polished ({total_fixes} fixes)",
            event_type="info",
            phase="compiling",
        )

    final_draft = clean_ai_language(final_draft)
    final_draft = strip_meta_text(final_draft)
    if not modern_shell:
        final_draft = localize_chapter_headings(final_draft, ctx.language)
    final_md_path.write_text(final_draft, encoding="utf-8")

    if ctx.verbose:
        print(f"\u2705 Draft compiled: {len(final_draft):,} characters")

    # ====================================================================
    # EXPORT
    # ====================================================================
    if ctx.verbose:
        print("\n📄 PHASE 5: EXPORT")

    if ctx.tracker:
        ctx.tracker.log_activity(
            "📄 Starting document export", event_type="milestone", phase="exporting"
        )
        ctx.tracker.update_exporting(export_type="PDF and DOCX")
        ctx.tracker.check_cancellation()

    # PDF export
    pdf_path = ctx.folders["exports"] / f"{base_filename}.pdf"

    if ctx.tracker:
        ctx.tracker.log_activity(
            "📑 Generating professional PDF document...",
            event_type="info",
            phase="exporting",
        )

    if ctx.verbose:
        print("📄 Exporting PDF (professional formatting)...")

    pdf_success, pdf_error = export_pdf(
        md_file=final_md_path,
        output_pdf=pdf_path,
        engine="pandoc",
        document_language=lang_base,
    )

    if not pdf_success:
        detail = (pdf_error or "").strip() or "unknown (see worker logs)"
        if len(detail) > 4000:
            detail = detail[:4000] + "\n…(truncated; full message in worker logs)"
        raise RuntimeError(f"PDF export failed: {detail}")
    if not pdf_path.exists():
        raise RuntimeError(f"PDF export failed - file not created: {pdf_path}")

    if ctx.tracker:
        ctx.tracker.log_activity(
            "\u2705 PDF document ready", event_type="found", phase="exporting"
        )
        ctx.tracker.log_activity(
            "📝 Creating Word document...", event_type="info", phase="exporting"
        )

    # DOCX export
    docx_path = ctx.folders["exports"] / f"{base_filename}.docx"
    docx_success = export_docx(md_file=final_md_path, output_docx=docx_path)

    if not docx_success or not docx_path.exists():
        raise RuntimeError(f"DOCX export failed - file not created: {docx_path}")

    if ctx.tracker:
        ctx.tracker.log_activity(
            "\u2705 Word document ready", event_type="found", phase="exporting"
        )

    # ZIP bundle
    zip_path = ctx.folders["exports"] / f"{base_filename}.zip"
    try:
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(pdf_path, pdf_path.name)
            zf.write(docx_path, docx_path.name)
            zf.write(final_md_path, final_md_path.name)
        if ctx.tracker:
            ctx.tracker.log_activity(
                "📦 ZIP bundle created", event_type="found", phase="exporting"
            )
    except Exception as zip_error:
        logger.warning(f"ZIP creation failed (non-critical): {zip_error}")

    if ctx.tracker:
        ctx.tracker.log_activity(
            "\u2705 Word document generated", event_type="found", phase="exporting"
        )
        ctx.tracker.log_activity(
            "🎉 Thesis generation complete!", event_type="milestone", phase="completed"
        )

    if ctx.verbose:
        print(f"\u2705 Exported PDF: {pdf_path}")
        print(f"\u2705 Exported DOCX: {docx_path}")
        print(f"📂 Output folder: {ctx.folders['root']}")

    return pdf_path, docx_path


# ---------------------------------------------------------------------------
# Helper functions (only used by compile phase)
# ---------------------------------------------------------------------------


def _strip_first_header(text: str) -> str:
    """Remove first line if it's a markdown header."""
    lines = text.strip().split("\n")
    if lines and lines[0].startswith("#"):
        return "\n".join(lines[1:]).strip()
    return text.strip()


def fix_single_line_tables(content: str) -> str:
    """
    Fix tables that LLM outputs on a single line.

    BUG #15: LLM sometimes generates tables as single concatenated lines:
    | Col1 | Col2 | | Row1 | Data | | Row2 | Data |
    """
    lines = content.split("\n")
    fixed_lines = []

    for line in lines:
        if line.strip().startswith("|") and re.search(r"\|\s*\|[:\w*]", line):
            parts = re.split(r"\| \|(?=\s*[:*\w-])", line)
            for part in parts:
                if part.strip():
                    fixed_part = part.strip()
                    if not fixed_part.startswith("|"):
                        fixed_part = "| " + fixed_part
                    if not fixed_part.endswith("|"):
                        fixed_part = fixed_part + " |"
                    fixed_lines.append(fixed_part)
        else:
            fixed_lines.append(line)

    return "\n".join(fixed_lines)


def deduplicate_appendices(content: str) -> str:
    """Remove duplicate appendix sections from draft content."""
    appendix_pattern = re.compile(
        r"(## Appendix [A-Z]:.*?)(?=## Appendix [A-Z]:|## References|# \d+\.|$)",
        re.DOTALL,
    )

    seen_headers = set()
    matches = list(appendix_pattern.finditer(content))

    for match in reversed(matches):
        appendix_text = match.group(1)
        header_match = re.match(r"## Appendix ([A-Z]):", appendix_text)
        if header_match:
            header = header_match.group(1)
            if header in seen_headers:
                start, end = match.span()
                content = content[:start] + content[end:]
            else:
                seen_headers.add(header)

    return content


def clean_malformed_markdown(content: str) -> str:
    """
    Clean up common markdown formatting issues.

    Fixes orphaned code fences, multiple blank lines, trailing whitespace.
    """
    lines = content.split("\n")
    fence_count = 0
    fence_positions = []

    for i, line in enumerate(lines):
        if line.strip() == "```":
            fence_count += 1
            fence_positions.append(i)

    if fence_count % 2 == 1 and fence_positions:
        last_fence = fence_positions[-1]
        lines[last_fence] = ""

    content = "\n".join(lines)
    content = re.sub(r"\n{4,}", "\n\n\n", content)
    content = re.sub(r"[ \t]+$", "", content, flags=re.MULTILINE)

    return content
