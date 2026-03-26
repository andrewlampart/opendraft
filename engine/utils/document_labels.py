#!/usr/bin/env python3
"""
Localized document type strings for structure (Architect) and compile/export metadata.
Internal academic_level keys stay: research_paper, bachelor, master, phd.
"""

from __future__ import annotations


def _lang_base(language: str) -> str:
    base = (language or "en").split("-")[0].lower()
    return base if base in ("en", "pl") else "en"


def document_type_for_outline(academic_level: str, language: str) -> str:
    """Phrase embedded in Architect outline_context (English or Polish)."""
    lk = _lang_base(language)
    en = {
        "research_paper": "short publication-style research draft (article length)",
        "bachelor": "bachelor's thesis",
        "master": "master's thesis",
        "phd": "PhD dissertation",
    }
    pl = {
        "research_paper": "draft publikacji naukowej (zakres artykułu)",
        "bachelor": "praca licencjacka",
        "master": "praca magisterska",
        "phd": "rozprawa doktorska",
    }
    table = pl if lk == "pl" else en
    return table.get(academic_level, table["master"])


def draft_type_export_label(academic_level: str, language: str) -> str:
    """project_type / cover-style draft type label."""
    lk = _lang_base(language)
    en = {
        "research_paper": "Publication draft",
        "bachelor": "Bachelor thesis",
        "master": "Master thesis",
        "phd": "Doctoral dissertation",
    }
    pl = {
        "research_paper": "Draft publikacji",
        "bachelor": "Praca licencjacka",
        "master": "Praca magisterska",
        "phd": "Praca doktorska",
    }
    table = pl if lk == "pl" else en
    return table.get(academic_level, table["master"])


def degree_export_label(academic_level: str, language: str) -> str:
    """YAML degree field (generic academic degree line)."""
    lk = _lang_base(language)
    en = {
        "research_paper": "Research publication",
        "bachelor": "Bachelor of Science",
        "master": "Master of Science",
        "phd": "Doctor of Philosophy",
    }
    pl = {
        "research_paper": "Publikacja naukowa",
        "bachelor": "Licencjat",
        "master": "Magisterium",
        "phd": "Doktorat",
    }
    table = pl if lk == "pl" else en
    return table.get(academic_level, table["master"])


def expose_strings(language: str) -> dict:
    """User-visible strings for research exposé markdown (EN or PL)."""
    lk = _lang_base(language)
    if lk == "pl":
        return {
            "doc_heading": "Eksponat badawczy",
            "lbl_generated": "Wygenerowano",
            "lbl_doc_type": "Typ dokumentu",
            "lbl_language": "Język",
            "h_executive": "Streszczenie wykonawcze",
            "p_executive": (
                'Niniejszy eksponat przedstawia wstępny przegląd tematu "{topic}" '
                "na podstawie analizy {n} źródeł naukowych. Zawiera uporządkowany konspekt "
                "możliwej pełnej pracy oraz bibliografię."
            ),
            "h_sources": "Przegląd źródeł",
            "tbl_metric": "Wskaźnik",
            "tbl_value": "Wartość",
            "row_total": "Łączna liczba źródeł",
            "row_years": "Lata publikacji",
            "row_recent": "Udział źródeł z ostatnich 5 lat",
            "row_recent_suffix": "z ostatnich 5 lat",
            "row_authors": "Unikalni autorzy",
            "row_toptier": "Źródła z czasopism top-tier",
            "row_journals": "Kluczowe czasopisma",
            "row_teams": "Kluczowe zespoły",
            "unit_papers": "recenzowanych publikacji",
            "unit_researchers": "badaczy",
            "p_sources_blurb": (
                "Eksponat syntetyzuje ustalenia {authors} badaczy z {journals} czasopism. "
                "{recency}% źródeł pochodzi z ostatnich 5 lat, co wskazuje na aktualność tematu."
            ),
            "h_outline": "Konspekt pracy",
            "h_findings": "Kluczowe ustalenia z literatury",
            "h_gaps": "Zidentyfikowane luki badawcze",
            "h_bib": "Bibliografia",
            "h_next": "Dalsze kroki",
            "p_next_intro": (
                "Ten eksponat jest punktem wyjścia do przygotowania pełnego dokumentu: "
                "**{doc_type}**. Aby rozwinąć go w pełny draft:"
            ),
            "next_1": "Rozwiń konspekt w treść rozdziałów",
            "next_2": "Pogłęb analizę wskazanych źródeł",
            "next_3": "Odnieś się do zidentyfikowanych luk badawczych",
            "next_4": "Opracuj oryginalne argumenty oparte na przeglądzie literatury",
            "footer": (
                "*Eksponat został wygenerowany jako przegląd badawczy — narzędzie planistyczne "
                "i punkt wyjścia do dalszej pracy.*"
            ),
            "year_range_various": "Różne",
            "fallback_journals": "Wiele źródeł",
            "fallback_researchers": "Wielu badaczy",
        }
    return {
        "doc_heading": "Research Expose",
        "lbl_generated": "Generated",
        "lbl_doc_type": "Document type",
        "lbl_language": "Language",
        "h_executive": "Executive Summary",
        "p_executive": (
            'This research expose provides a preliminary overview of the topic "{topic}" '
            "based on an analysis of {n} academic sources. It includes a structured outline "
            "for a potential full document and a comprehensive bibliography."
        ),
        "h_sources": "Research Sources Overview",
        "tbl_metric": "Metric",
        "tbl_value": "Value",
        "row_total": "Total Sources",
        "row_years": "Publication Years",
        "row_recent": "Recent Sources",
        "row_recent_suffix": "from last 5 years",
        "row_authors": "Unique Authors",
        "row_toptier": "Top-Tier Journals",
        "row_journals": "Key Journals",
        "row_teams": "Key Research Teams",
        "unit_papers": "peer-reviewed papers",
        "unit_researchers": "researchers",
        "p_sources_blurb": (
            "This expose synthesizes findings from {authors} researchers across {journals} journals. "
            "{recency}% of sources are from the last 5 years, indicating current research relevance."
        ),
        "h_outline": "Research Outline",
        "h_findings": "Key Research Findings",
        "h_gaps": "Identified Research Gaps",
        "h_bib": "Bibliography",
        "h_next": "Next Steps",
        "p_next_intro": (
            "This research expose serves as a starting point for a comprehensive **{doc_type}**. "
            "To develop this into a full draft:"
        ),
        "next_1": "Expand the outline into detailed chapter content",
        "next_2": "Conduct deeper analysis of the identified sources",
        "next_3": "Address the research gaps highlighted above",
        "next_4": "Develop original arguments based on the literature review",
        "footer": (
            "*This expose was generated as a research overview. It is intended as a planning tool "
            "and starting point for further development.*"
        ),
        "year_range_various": "Various",
        "fallback_journals": "Multiple sources",
        "fallback_researchers": "Multiple researchers",
    }
