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
from typing import Tuple
from datetime import datetime

from .context import DraftContext

logger = logging.getLogger(__name__)


def run_expose_export(ctx: DraftContext) -> Tuple[Path, Path]:
    """
    Handle expose mode: generate research overview + outline only.

    Returns: (pdf_path, docx_path)
    """
    from utils.export_professional import export_pdf, export_docx
    from draft_generator import slugify, get_language_name

    logger.info("=" * 80)
    logger.info("EXPOSE MODE: Generating research overview (skipping full draft)")
    logger.info("=" * 80)

    if ctx.tracker:
        ctx.tracker.log_activity("📋 Creating Research Expose...", event_type="milestone", phase="exporting")
        ctx.tracker.update_phase("exporting", progress_percent=70, details={"stage": "creating_expose"})

    language_name = get_language_name(ctx.language)
    _lang = (ctx.language or 'en').split('-')[0].lower()

    if ctx.verbose:
        print("\n📋 EXPOSE MODE: Creating research overview...")

    # Localized expose labels
    _expose_labels = {
        'en': {
            'title_prefix': 'Research Expose',
            'generated': 'Generated',
            'academic_level': 'Academic Level',
            'language': 'Language',
            'executive_summary': 'Executive Summary',
            'executive_summary_text': f'This research expose provides a preliminary overview of the topic "{ctx.topic}" based on an analysis of {len(ctx.citation_database.citations)} academic sources. It includes a structured outline for a potential full research paper and a comprehensive bibliography.',
            'research_outline': 'Research Outline',
            'key_findings': 'Key Research Findings',
            'research_gaps': 'Identified Research Gaps',
            'bibliography': 'Bibliography',
            'next_steps': 'Next Steps',
            'next_steps_text': f'This research expose serves as a starting point for a comprehensive {ctx.academic_level}-level paper. To develop this into a full draft:',
            'step_1': 'Expand the outline into detailed chapter content',
            'step_2': 'Conduct deeper analysis of the identified sources',
            'step_3': 'Address the research gaps highlighted above',
            'step_4': 'Develop original arguments based on the literature review',
            'footer': 'This expose was generated as a research overview. It is intended as a planning tool and starting point for further development.',
        },
        'pl': {
            'title_prefix': 'Ekspoze badawcze',
            'generated': 'Wygenerowano',
            'academic_level': 'Poziom akademicki',
            'language': 'Język',
            'executive_summary': 'Podsumowanie',
            'executive_summary_text': f'Niniejsze ekspoze badawcze stanowi wstępny przegląd tematu „{ctx.topic}" na podstawie analizy {len(ctx.citation_database.citations)} źródeł akademickich. Zawiera zarys struktury potencjalnej pełnej pracy badawczej oraz obszerną bibliografię.',
            'research_outline': 'Zarys pracy',
            'key_findings': 'Kluczowe wyniki badań',
            'research_gaps': 'Zidentyfikowane luki badawcze',
            'bibliography': 'Bibliografia',
            'next_steps': 'Następne kroki',
            'next_steps_text': f'Niniejsze ekspoze stanowi punkt wyjścia do opracowania pełnej pracy na poziomie {ctx.academic_level}. Aby rozwinąć je w kompletną pracę:',
            'step_1': 'Rozwinąć zarys w szczegółową treść rozdziałów',
            'step_2': 'Przeprowadzić pogłębioną analizę zidentyfikowanych źródeł',
            'step_3': 'Odnieść się do wskazanych powyżej luk badawczych',
            'step_4': 'Opracować oryginalne argumenty na podstawie przeglądu literatury',
            'footer': 'Niniejsze ekspoze zostało wygenerowane jako przegląd badawczy. Służy jako narzędzie planistyczne i punkt wyjścia do dalszych prac.',
        },
        'de': {
            'title_prefix': 'Forschungsexposé',
            'generated': 'Erstellt',
            'academic_level': 'Akademisches Niveau',
            'language': 'Sprache',
            'executive_summary': 'Zusammenfassung',
            'executive_summary_text': f'Dieses Forschungsexposé bietet einen vorläufigen Überblick über das Thema „{ctx.topic}" basierend auf einer Analyse von {len(ctx.citation_database.citations)} akademischen Quellen.',
            'research_outline': 'Forschungsgliederung',
            'key_findings': 'Wichtige Forschungsergebnisse',
            'research_gaps': 'Identifizierte Forschungslücken',
            'bibliography': 'Literaturverzeichnis',
            'next_steps': 'Nächste Schritte',
            'next_steps_text': f'Dieses Exposé dient als Ausgangspunkt für eine umfassende Arbeit auf {ctx.academic_level}-Niveau.',
            'step_1': 'Die Gliederung in detaillierte Kapitelinhalte ausbauen',
            'step_2': 'Eine vertiefte Analyse der identifizierten Quellen durchführen',
            'step_3': 'Die oben genannten Forschungslücken adressieren',
            'step_4': 'Eigenständige Argumente auf Basis der Literaturübersicht entwickeln',
            'footer': 'Dieses Exposé wurde als Forschungsüberblick erstellt. Es dient als Planungsinstrument und Ausgangspunkt für die weitere Bearbeitung.',
        },
    }
    el = _expose_labels.get(_lang, _expose_labels['en'])

    # Compile the expose document
    expose_content = f"""# {el['title_prefix']}: {ctx.topic}

**{el['generated']}:** {datetime.now().strftime('%Y-%m-%d')}
**{el['academic_level']}:** {ctx.academic_level.title()}
**{el['language']}:** {language_name}

---

## {el['executive_summary']}

{el['executive_summary_text']}

---

## {el['research_outline']}

{ctx.formatter_output}

---

## {el['key_findings']}

{ctx.scribe_output[:4000] if len(ctx.scribe_output) > 4000 else ctx.scribe_output}

---

## {el['research_gaps']}

{ctx.signal_output[:2000] if len(ctx.signal_output) > 2000 else ctx.signal_output}

---

## {el['bibliography']}

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

## {el['next_steps']}

{el['next_steps_text']}

1. **{el['step_1']}**
2. **{el['step_2']}**
3. **{el['step_3']}**
4. **{el['step_4']}**

---

*{el['footer']}*
"""

    # Save expose markdown
    expose_md_path = ctx.folders['drafts'] / "00_expose.md"
    expose_md_path.write_text(expose_content, encoding='utf-8')
    logger.info(f"Expose markdown saved: {expose_md_path}")

    if ctx.tracker:
        ctx.tracker.log_activity("📄 Exporting Research Expose...", event_type="info", phase="exporting")
        ctx.tracker.update_phase("exporting", progress_percent=85, details={"stage": "exporting_expose"})

    # Export as PDF and DOCX
    topic_slug = slugify(ctx.topic, max_length=50)
    if not topic_slug:
        topic_slug = "research_expose"

    if ctx.verbose:
        print("📄 Exporting PDF...")

    pdf_path = ctx.folders['exports'] / f"{topic_slug}_expose.pdf"
    pdf_success = export_pdf(md_file=expose_md_path, output_pdf=pdf_path, engine='pandoc')

    if not pdf_success or not pdf_path.exists():
        raise RuntimeError(f"PDF export failed for expose: {pdf_path}")

    if ctx.verbose:
        print("📝 Exporting Word document...")

    docx_path = ctx.folders['exports'] / f"{topic_slug}_expose.docx"
    docx_success = export_docx(md_file=expose_md_path, output_docx=docx_path)

    if not docx_success or not docx_path.exists():
        raise RuntimeError(f"DOCX export failed for expose: {docx_path}")

    if ctx.tracker:
        ctx.tracker.log_activity("🎉 Research Expose complete!", event_type="milestone", phase="completed")
        ctx.tracker.update_phase(
            "exporting",
            progress_percent=100,
            sources_count=len(ctx.citation_database.citations),
            chapters_count=1,
            details={"stage": "expose_complete", "milestone": "expose_complete"},
        )

    if ctx.verbose:
        print(f"\n\u2705 Research Expose complete!")
        print(f"   PDF: {pdf_path}")
        print(f"   DOCX: {docx_path}")

    return pdf_path, docx_path


def run_compile_and_export(ctx: DraftContext) -> Tuple[Path, Path]:
    """
    Execute the compile and export phase: assemble draft, generate abstract, export.

    Returns: (pdf_path, docx_path)
    """
    from utils.agent_runner import run_agent
    from utils.citation_compiler import CitationCompiler
    from utils.abstract_generator import generate_abstract_for_draft
    from utils.export_professional import export_pdf, export_docx
    from utils.text_utils import clean_ai_language, strip_meta_text, localize_chapter_headings, clean_agent_output
    from utils.text_cleanup import apply_full_cleanup
    from draft_generator import slugify, get_chapter_name

    if ctx.verbose:
        print("\n🔧 PHASE 4: COMPILE")

    if ctx.tracker:
        ctx.tracker.log_activity("🔧 Starting document compilation", event_type="milestone", phase="compiling")
        ctx.tracker.update_phase("compiling", progress_percent=75, details={"stage": "assembling_draft"})
        ctx.tracker.check_cancellation()

    # Strip headers from section outputs (clean_agent_output removes preambles/metadata/cite_MISSING)
    intro_clean = _strip_first_header(clean_agent_output(ctx.intro_output))
    body_clean = _strip_first_header(clean_agent_output(ctx.body_output))
    conclusion_clean = _strip_first_header(clean_agent_output(ctx.conclusion_output))

    appendices_file = ctx.folders['drafts'] / "04_appendices.md"
    if appendices_file.exists():
        appendix_content = appendices_file.read_text(encoding='utf-8')
        appendix_clean = _strip_first_header(clean_agent_output(appendix_content))
    else:
        appendix_clean = ""

    current_date = datetime.now().strftime("%B %Y")

    # Calculate word count / pages
    draft_text = f"{intro_clean}\n{body_clean}\n{conclusion_clean}\n{appendix_clean}"
    word_count = len(draft_text.split())
    pages_estimate = word_count // 250

    # Labels — localized by language
    lang_code = (ctx.language or 'en').split('-')[0].lower()

    _draft_type_labels = {
        'en': {
            'research_paper': 'Research Paper',
            'bachelor': 'Bachelor Draft',
            'master': 'Master Draft',
            'phd': 'PhD Dissertation',
        },
        'pl': {
            'research_paper': 'Praca badawcza',
            'bachelor': 'Praca licencjacka',
            'master': 'Praca magisterska',
            'phd': 'Rozprawa doktorska',
        },
        'de': {
            'research_paper': 'Forschungsarbeit',
            'bachelor': 'Bachelorarbeit',
            'master': 'Masterarbeit',
            'phd': 'Dissertation',
        },
    }
    draft_type = _draft_type_labels.get(lang_code, _draft_type_labels['en']).get(
        ctx.academic_level, _draft_type_labels['en'].get(ctx.academic_level, 'Master Draft')
    )

    _degree_labels = {
        'en': {
            'research_paper': 'Research Paper',
            'bachelor': 'Bachelor of Science',
            'master': 'Master of Science',
            'phd': 'Doctor of Philosophy',
        },
        'pl': {
            'research_paper': 'Praca badawcza',
            'bachelor': 'Licencjat',
            'master': 'Magister',
            'phd': 'Doktor',
        },
        'de': {
            'research_paper': 'Forschungsarbeit',
            'bachelor': 'Bachelor of Science',
            'master': 'Master of Science',
            'phd': 'Doktor',
        },
    }
    degree = _degree_labels.get(lang_code, _degree_labels['en']).get(
        ctx.academic_level, _degree_labels['en'].get(ctx.academic_level, 'Master of Science')
    )

    # YAML metadata — use empty strings instead of English placeholders for non-English languages
    _default_department = {"en": "Department of Computer Science", "pl": "Katedra", "de": "Institut"}
    _default_faculty = {"en": "Faculty of Engineering", "pl": "Wydział", "de": "Fakultät"}
    _default_location = {"en": "Munich", "pl": "", "de": "München"}

    yaml_author = ctx.author_name or "OpenDraft AI"
    yaml_institution = ctx.institution or ""
    yaml_department = ctx.department or _default_department.get(lang_code, "")
    yaml_faculty = ctx.faculty or _default_faculty.get(lang_code, "")
    yaml_advisor = ctx.advisor or ""
    yaml_second_examiner = ctx.second_examiner or ""
    yaml_location = ctx.location or _default_location.get(lang_code, "")
    yaml_student_id = ctx.student_id or ""

    # Localized section headers
    h_abstract = get_chapter_name('abstract', ctx.language)
    h_introduction = get_chapter_name('introduction', ctx.language)
    h_main_body = get_chapter_name('main_body', ctx.language)
    h_conclusion = get_chapter_name('conclusion', ctx.language)
    h_appendix = get_chapter_name('appendix', ctx.language)
    h_references = get_chapter_name('references', ctx.language)

    # Localized word count label
    word_count_label = "słów" if lang_code == 'pl' else "Wörter" if lang_code == 'de' else "palabras" if lang_code == 'es' else "mots" if lang_code == 'fr' else "words"

    # Localized abstract placeholder
    abstract_placeholder_map = {
        'pl': '[Streszczenie zostanie wygenerowane]',
        'de': '[Zusammenfassung wird automatisch generiert]',
    }
    abstract_placeholder = abstract_placeholder_map.get(lang_code, '[Abstract will be generated]')

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
word_count: "{word_count:,} {word_count_label}"
pages: "{pages_estimate}"
generated_by: "OpenDraft AI - https://github.com/federicodeponte/opendraft"
---

## {h_abstract}
{abstract_placeholder}

\\newpage

# 1. {h_introduction}
{intro_clean}

\\newpage

# 2. {h_main_body}
{body_clean}

\\newpage

# 3. {h_conclusion}
{conclusion_clean}

\\newpage

# 4. {h_appendix}
{appendix_clean}

\\newpage

# 5. {h_references}
[Citations will be compiled]
"""

    # Citation compilation
    if ctx.tracker:
        ctx.tracker.log_activity("📚 Compiling citations and references...", event_type="info", phase="compiling")

    compiler = CitationCompiler(database=ctx.citation_database, model=ctx.model)
    reference_list = compiler.generate_reference_list(full_draft)
    compiled_draft, replaced_ids, failed_ids = compiler.compile_citations(full_draft, research_missing=True, verbose=ctx.verbose)

    if ctx.tracker:
        ctx.tracker.log_activity(f"\u2705 Citations compiled ({len(replaced_ids)} references)", event_type="found", phase="compiling")

    # Remove template References section and append generated one
    compiled_draft = re.sub(
        r'^\s*#+ (?:\d+\.\s*)?(?:References|Bibliography|Bibliografia|Literaturverzeichnis|Referencias)\s*\n\s*\[Citations will be compiled\]\s*',
        '',
        compiled_draft,
        flags=re.MULTILINE,
    )
    compiled_draft = compiled_draft + reference_list

    # Save intermediate draft for abstract generation
    intermediate_md_path = ctx.folders['exports'] / "INTERMEDIATE_DRAFT.md"
    intermediate_md_path.write_text(compiled_draft, encoding='utf-8')

    # Generate abstract
    if ctx.tracker:
        ctx.tracker.log_activity("📝 Generating abstract...", event_type="info", phase="compiling")

    abstract_success, abstract_updated_content = generate_abstract_for_draft(
        draft_path=intermediate_md_path,
        model=ctx.model,
        run_agent_func=run_agent,
        output_dir=ctx.folders['exports'],
        verbose=ctx.verbose,
    )

    if ctx.tracker:
        ctx.tracker.log_activity("\u2705 Abstract generated", event_type="found", phase="compiling")

    final_draft = abstract_updated_content if abstract_success and abstract_updated_content else compiled_draft

    # Generate filename
    base_filename = slugify(ctx.topic, max_length=50)
    if not base_filename:
        base_filename = "research_paper"

    # Clean and save final markdown
    final_md_path = ctx.folders['exports'] / f"{base_filename}.md"
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
        print(f"   ✨ Text cleanup: {total_fixes} fixes (fillers={cleanup_stats['fillers']}, "
              f"vocab={cleanup_stats['vocab_diversified']}, claims={cleanup_stats['claims_calibrated']})")

    if ctx.tracker and total_fixes > 0:
        ctx.tracker.log_activity(
            f"✨ Prose polished ({total_fixes} fixes)",
            event_type="info",
            phase="compiling"
        )

    final_draft = clean_ai_language(final_draft)
    final_draft = strip_meta_text(final_draft)
    final_draft = localize_chapter_headings(final_draft, ctx.language)
    final_md_path.write_text(final_draft, encoding='utf-8')

    if ctx.verbose:
        print(f"\u2705 Draft compiled: {len(final_draft):,} characters")

    # ====================================================================
    # EXPORT
    # ====================================================================
    if ctx.verbose:
        print("\n📄 PHASE 5: EXPORT")

    if ctx.tracker:
        ctx.tracker.log_activity("📄 Starting document export", event_type="milestone", phase="exporting")
        ctx.tracker.update_exporting(export_type="PDF and DOCX")
        ctx.tracker.check_cancellation()

    # PDF export
    pdf_path = ctx.folders['exports'] / f"{base_filename}.pdf"

    if ctx.tracker:
        ctx.tracker.log_activity("📑 Generating professional PDF document...", event_type="info", phase="exporting")

    if ctx.verbose:
        print("📄 Exporting PDF (professional formatting)...")

    # PDF: try Pandoc first, fallback to LibreOffice (engine='auto')
    pdf_success = export_pdf(md_file=final_md_path, output_pdf=pdf_path, engine='auto')

    # DOCX export - always run so user has editable format even if PDF fails
    docx_path = ctx.folders['exports'] / f"{base_filename}.docx"
    docx_success = export_docx(md_file=final_md_path, output_docx=docx_path)

    if not docx_success or not docx_path.exists():
        raise RuntimeError(f"DOCX export failed - file not created: {docx_path}")

    if pdf_success and pdf_path.exists():
        if ctx.tracker:
            ctx.tracker.log_activity("\u2705 PDF document ready", event_type="found", phase="exporting")
    else:
        if ctx.verbose:
            print("⚠️  PDF export failed - DOCX and Markdown available. Install Pandoc+LaTeX or LibreOffice for PDF.")

    if ctx.tracker:
        ctx.tracker.log_activity("\u2705 Word document ready", event_type="found", phase="exporting")

    # ZIP bundle (include PDF only if generated)
    zip_path = ctx.folders['exports'] / f"{base_filename}.zip"
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            if pdf_path.exists():
                zf.write(pdf_path, pdf_path.name)
            zf.write(docx_path, docx_path.name)
            zf.write(final_md_path, final_md_path.name)
        if ctx.tracker:
            ctx.tracker.log_activity("📦 ZIP bundle created", event_type="found", phase="exporting")
    except Exception as zip_error:
        logger.warning(f"ZIP creation failed (non-critical): {zip_error}")

    if ctx.tracker:
        ctx.tracker.log_activity("\u2705 Word document generated", event_type="found", phase="exporting")
        ctx.tracker.log_activity("🎉 Thesis generation complete!", event_type="milestone", phase="completed")

    if ctx.verbose:
        if pdf_path.exists():
            print(f"\u2705 Exported PDF: {pdf_path}")
        print(f"\u2705 Exported DOCX: {docx_path}")
        print(f"📂 Output folder: {ctx.folders['root']}")

    return pdf_path, docx_path


# ---------------------------------------------------------------------------
# Helper functions (only used by compile phase)
# ---------------------------------------------------------------------------


def _strip_first_header(text: str) -> str:
    """Remove first line if it's a markdown header."""
    lines = text.strip().split('\n')
    if lines and lines[0].startswith('#'):
        return '\n'.join(lines[1:]).strip()
    return text.strip()


def fix_single_line_tables(content: str) -> str:
    """
    Fix tables that LLM outputs on a single line.

    BUG #15: LLM sometimes generates tables as single concatenated lines:
    | Col1 | Col2 | | Row1 | Data | | Row2 | Data |
    """
    lines = content.split('\n')
    fixed_lines = []

    for line in lines:
        if line.strip().startswith('|') and re.search(r'\|\s*\|[:\w*]', line):
            parts = re.split(r'\| \|(?=\s*[:*\w-])', line)
            for part in parts:
                if part.strip():
                    fixed_part = part.strip()
                    if not fixed_part.startswith('|'):
                        fixed_part = '| ' + fixed_part
                    if not fixed_part.endswith('|'):
                        fixed_part = fixed_part + ' |'
                    fixed_lines.append(fixed_part)
        else:
            fixed_lines.append(line)

    return '\n'.join(fixed_lines)


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
