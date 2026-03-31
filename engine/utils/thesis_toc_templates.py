"""
TOC template catalog for thesis generation: skeleton outlines, compose headings,
compile behavior, and literature vs empirical prompt fragments.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

TEMPLATE_DEFAULT = "default"
TEMPLATE_CLASSIC_SOCIAL = "classic_social"
TEMPLATE_CASE_STUDY = "case_study"
TEMPLATE_IMRAD = "imrad_science"
TEMPLATE_BUSINESS = "business_mgmt"

WORK_MODE_LITERATURE = "literature_review"
WORK_MODE_EMPIRICAL = "empirical"

VALID_TEMPLATES = frozenset(
    {
        TEMPLATE_DEFAULT,
        TEMPLATE_CLASSIC_SOCIAL,
        TEMPLATE_CASE_STUDY,
        TEMPLATE_IMRAD,
        TEMPLATE_BUSINESS,
    }
)


def normalize_toc_options(raw: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    base = {
        "include_abbreviations": False,
        "include_figures_tables": True,
        "include_annex": True,
        "numbering": "roman_arabic",
    }
    if not raw:
        return dict(base)
    out = {**base, **raw}
    if out.get("numbering") not in ("roman_arabic", "arabic_only"):
        out["numbering"] = "roman_arabic"
    for k in ("include_abbreviations", "include_figures_tables", "include_annex"):
        out[k] = bool(out.get(k, base[k]))
    return out


def normalize_template_id(tid: Optional[str]) -> str:
    t = (tid or TEMPLATE_DEFAULT).strip()
    return t if t in VALID_TEMPLATES else TEMPLATE_DEFAULT


@dataclass
class ThesisTocSpec:
    template_id: str
    use_legacy_document_shell: bool
    skip_discussion_agent: bool
    """If True, discussion slot is not called; merge uses empty discussion."""
    empirical_placeholder_for_results: bool
    """When empirical mode and no user_results_markdown, skip LLM results and insert placeholder."""
    skeleton_outline_pl: str
    skeleton_outline_en: str
    numbering_instruction_pl: str
    numbering_instruction_en: str
    intro_instruction_pl: str
    intro_instruction_en: str
    intro_extra_pl: str = ""
    intro_extra_en: str = ""
    lit_review_instruction_pl: str = ""
    lit_review_instruction_en: str = ""
    methodology_instruction_pl: str = ""
    methodology_instruction_en: str = ""
    results_instruction_pl: str = ""
    results_instruction_en: str = ""
    discussion_instruction_pl: str = ""
    discussion_instruction_en: str = ""
    conclusion_instruction_pl: str = ""
    conclusion_instruction_en: str = ""
    appendix_instruction_pl: str = ""
    appendix_instruction_en: str = ""
    references_heading_pl: str = "Bibliografia"
    references_heading_en: str = "References"
    abbreviations_heading_pl: str = "Wykaz skrótów"
    abbreviations_heading_en: str = "List of Abbreviations"
    list_figures_heading_pl: str = "Spis rysunków"
    list_figures_heading_en: str = "List of Figures"
    list_tables_heading_pl: str = "Spis tabel"
    list_tables_heading_en: str = "List of Tables"


def _numbering_block(lang: str, numbering: str) -> str:
    if numbering == "arabic_only":
        if lang == "pl":
            return (
                "Numeracja: używaj wyłącznie arabskiej — główne rozdziały 1., 2., … "
                "oraz podrozdziały 1.1., 1.1.1. itd. Nie używaj cyfr rzymskich w nagłówkach."
            )
        return (
            "Numbering: use Arabic only for all section levels (1., 1.1., 1.1.1.). "
            "Do not use Roman numerals in headings."
        )
    if lang == "pl":
        return (
            "Numeracja: rozdziały główne mogą być oznaczone cyframi rzymskimi (I., II., …) "
            "w etykiecie „Rozdział I” itd.; podrozdziały arabskie (1.1., 1.2., …) zgodnie ze szkieletem."
        )
    return (
        "Numbering: main chapters may use Roman numerals in labels (Chapter I, II, …); "
        "subsections use Arabic (1.1., 1.2.) per skeleton."
    )


_SKELETON_CLASSIC_PL = """Wstęp
Rozdział I. [Tytuł rozdziału teoretycznego — dostosuj do tematu]
1.1. Definicje i pojęcia podstawowe
1.2. Uwarunkowania zjawiska
1.3. Funkcje i modele
Rozdział II. [Drugi rozdział teoretyczny — szerszy kontekst]
2.1. Dane i statystyki
2.2. Czynniki wpływające na zjawisko
2.3. Skutki zjawiska
Rozdział III. Metodologia badań własnych
3.1. Przedmiot i cel badań
3.2. Pytania i hipotezy badawcze
3.3. Metoda, technika i narzędzie badawcze
3.4. Teren i organizacja badań
Rozdział IV. Analiza wyników badań własnych
4.1. Charakterystyka grupy badawczej
4.2. Wyniki badań (analiza danych)
4.3. Weryfikacja hipotez i wnioski
Zakończenie
Bibliografia
Spis tabel i rysunków
Aneks"""

_SKELETON_CLASSIC_EN = """Introduction
Chapter I. [Theoretical chapter title — adapt to topic]
1.1. Definitions and basic concepts
1.2. Determinants of the phenomenon
1.3. Functions and models
Chapter II. [Second theoretical chapter — broader context]
2.1. Data and statistics
2.2. Factors influencing the phenomenon
2.3. Consequences of the phenomenon
Chapter III. Methodology of own research
3.1. Subject and aim of the study
3.2. Research questions and hypotheses
3.3. Method, technique and research tools
3.4. Setting and organization of research
Chapter IV. Analysis of own research results
4.1. Characteristics of the study group
4.2. Research results (data analysis)
4.3. Hypothesis verification and conclusions
Conclusion
References
List of tables and figures
Annex"""

_SKELETON_CASE_PL = """Wykaz skrótów (opcjonalnie)
Wstęp
Rozdział 1. Charakterystyka [choroba/jednostka chorobowa]
1.1. Definicja i etiologia
1.2. Epidemiologia i czynniki ryzyka
1.3. Objawy i diagnozowanie
1.4. Metody leczenia i profilaktyka
Rozdział 2. Metodologia pracy
2.1. Cel pracy
2.2. Metody, techniki i narzędzia badawcze
Rozdział 3. Studium indywidualnego przypadku pacjenta
3.1. Opis przypadku (wywiad, stan pacjenta)
3.2. Model opieki / proces pielęgnowania (diagnozy, cele, interwencje)
3.3. Ocena uzyskanych wyników
Zakończenie / Wnioski
Bibliografia
Załączniki"""

_SKELETON_CASE_EN = """List of Abbreviations (optional)
Introduction
Chapter 1. Characteristics of [disease/clinical entity]
1.1. Definition and aetiology
1.2. Epidemiology and risk factors
1.3. Signs and diagnosis
1.4. Treatment and prevention
Chapter 2. Methodology of the work
2.1. Aim of the work
2.2. Methods, techniques and research tools
Chapter 3. Individual patient case study
3.1. Case description (history, patient status)
3.2. Care model / nursing process (diagnoses, goals, interventions)
3.3. Evaluation of outcomes
Conclusion / Implications
References
Appendices"""

_SKELETON_IMRAD_PL = """1. Wstęp
1.1. [Tło problemu]
1.2. [Aktualny stan wiedzy]
2. Cel badań
2.1. [Główny cel]
2.2. [Cele szczegółowe]
3. Materiały i metody
3.1. Materiały badawcze / odczynniki
3.2. Metody analityczne / laboratoryjne
3.3. Analiza statystyczna
4. Wyniki badań
4.1. [Analiza pierwszej zmiennej]
4.2. [Analiza kolejnych zmiennych]
5. Dyskusja
6. Wnioski
7. Piśmiennictwo / bibliografia"""

_SKELETON_IMRAD_EN = """1. Introduction
1.1. [Background]
1.2. [Current state of knowledge]
2. Aim of the study
2.1. [Main aim]
2.2. [Specific objectives]
3. Materials and methods
3.1. Materials / reagents
3.2. Analytical / laboratory methods
3.3. Statistical analysis
4. Results
4.1. [First variable]
4.2. [Further variables]
5. Discussion
6. Conclusions
7. References / bibliography"""

_SKELETON_BUSINESS_PL = """Wstęp
Rozdział I. [Podstawy teoretyczne branży/zjawiska]
1.1. Definicje i kluczowe pojęcia
1.2. Modele zarządzania / obsługa klienta w wybranej branży
1.3. Narzędzia i systemy
Rozdział II. Charakterystyka przedsiębiorstwa [Nazwa firmy]
2.1. Historia i rozwój firmy
2.2. Struktura organizacyjna
2.3. Pozycja rynkowa i konkurencja
Rozdział III. Analiza [procesu/zjawiska] na przykładzie firmy [Nazwa firmy]
3.1. Przebieg wybranego procesu
3.2. Identyfikacja problemów i wąskich gardeł
3.3. Proponowane rozwiązania / projekt optymalizacji
Zakończenie
Spis literatury
Spis rysunków i tabel"""

_SKELETON_BUSINESS_EN = """Introduction
Chapter I. [Theoretical foundations of industry/phenomenon]
1.1. Definitions and key concepts
1.2. Management models / customer service in the sector
1.3. Tools and systems
Chapter II. Profile of [Company name]
2.1. History and development
2.2. Organizational structure
2.3. Market position and competition
Chapter III. Analysis of [process/phenomenon] at [Company name]
3.1. Course of the selected process
3.2. Problems and bottlenecks
3.3. Proposed solutions / optimization design
Conclusion
List of references
List of figures and tables"""


def build_thesis_toc_spec(
    template_id: Optional[str],
    language: str,
    toc_options: Optional[Dict[str, Any]] = None,
) -> ThesisTocSpec:
    tid = normalize_template_id(template_id)
    opts = normalize_toc_options(toc_options)
    lang = (language or "en").split("-")[0].lower()
    if lang not in ("pl", "en"):
        lang = "en"
    num = opts["numbering"]
    nb_pl = _numbering_block("pl", num)
    nb_en = _numbering_block("en", num)

    if tid == TEMPLATE_DEFAULT:
        return ThesisTocSpec(
            template_id=tid,
            use_legacy_document_shell=True,
            skip_discussion_agent=False,
            empirical_placeholder_for_results=False,
            skeleton_outline_pl="",
            skeleton_outline_en="",
            numbering_instruction_pl=nb_pl,
            numbering_instruction_en=nb_en,
            intro_instruction_pl=(
                "Zacznij od nagłówka ## 1. Introduction lub ## Wstęp (zgodnie z językiem dokumentu). "
                "Nie dodawaj osobnego tytułu dokumentu."
            ),
            intro_instruction_en="Start with ## 1. Introduction. Do not add a separate document title.",
            lit_review_instruction_pl="## 2.1 Literatura — użyj podrozdziałów ### 2.1.1, ### 2.1.2 itd.",
            lit_review_instruction_en="## 2.1 Literature Review — use ### 2.1.1, ### 2.1.2, etc.",
            methodology_instruction_pl="## 2.2 Metodologia — ### 2.2.1 …",
            methodology_instruction_en="## 2.2 Methodology — ### 2.2.1 …",
            results_instruction_pl="## 2.3 Wyniki i analiza — ### 2.3.1 …",
            results_instruction_en="## 2.3 Analysis and Results — ### 2.3.1 …",
            discussion_instruction_pl="## 2.4 Dyskusja — odwołuj się do części teoretycznej i wyników.",
            discussion_instruction_en="## 2.4 Discussion — link to theory and results sections.",
            conclusion_instruction_pl="## Zakończenie lub ## 3. Conclusion wg konwencji dokumentu.",
            conclusion_instruction_en="## Conclusion or ## 3. Conclusion per document language.",
            appendix_instruction_pl="## Załączniki",
            appendix_instruction_en="## Appendices",
        )

    if tid == TEMPLATE_CLASSIC_SOCIAL:
        return ThesisTocSpec(
            template_id=tid,
            use_legacy_document_shell=False,
            skip_discussion_agent=False,
            empirical_placeholder_for_results=True,
            skeleton_outline_pl=_SKELETON_CLASSIC_PL,
            skeleton_outline_en=_SKELETON_CLASSIC_EN,
            numbering_instruction_pl=nb_pl,
            numbering_instruction_en=nb_en,
            intro_instruction_pl="# Wstęp — bez numeru rozdziału na tym poziomie; rozwinięcie teoretyczne wstępu.",
            intro_instruction_en="# Introduction — unnumbered top-level; set up the thesis.",
            lit_review_instruction_pl=(
                "Dwa rozdziały teoretyczne w jednej sekcji: "
                "## Rozdział I. [dostosuj tytuł do tematu] z ### 1.1. … ### 1.3.; "
                "następnie ## Rozdział II. [tytuł] z ### 2.1. … ### 2.3."
            ),
            lit_review_instruction_en=(
                "Two theoretical chapters in one section: "
                "## Chapter I. [adapt title] with ### 1.1.–1.3.; "
                "then ## Chapter II. [title] with ### 2.1.–2.3."
            ),
            methodology_instruction_pl=(
                "## Rozdział III. Metodologia badań własnych z ### 3.1.–3.4. zgodnie ze szkieletem."
            ),
            methodology_instruction_en="## Chapter III. Methodology of own research with ### 3.1.–3.4.",
            results_instruction_pl=(
                "## Rozdział IV. Analiza wyników badań własnych z ### 4.1. i ### 4.2. "
                "(sekcja 4.3 może być krótsza lub powiązana z następną częścią dyskusji)."
            ),
            results_instruction_en="## Chapter IV. Analysis of own results with ### 4.1. and ### 4.2.",
            discussion_instruction_pl=(
                "Kontynuuj w ramach Rozdziału IV: ### 4.3. Weryfikacja hipotez i wnioski — "
                "lub osobny blok pod tym samym rozdziałem."
            ),
            discussion_instruction_en="Continue Chapter IV: ### 4.3. Hypothesis verification and conclusions.",
            conclusion_instruction_pl="# Zakończenie",
            conclusion_instruction_en="# Conclusion",
            appendix_instruction_pl="# Aneks",
            appendix_instruction_en="# Annex",
            references_heading_pl="Bibliografia",
            references_heading_en="References",
        )

    if tid == TEMPLATE_CASE_STUDY:
        return ThesisTocSpec(
            template_id=tid,
            use_legacy_document_shell=False,
            skip_discussion_agent=True,
            empirical_placeholder_for_results=True,
            skeleton_outline_pl=_SKELETON_CASE_PL,
            skeleton_outline_en=_SKELETON_CASE_EN,
            numbering_instruction_pl=nb_pl,
            numbering_instruction_en=nb_en,
            intro_instruction_pl="# Wstęp",
            intro_instruction_en="# Introduction",
            lit_review_instruction_pl=(
                "## Rozdział 1. Charakterystyka [jednostka chorobowa z tematu] "
                "z ### 1.1.–1.4."
            ),
            lit_review_instruction_en="## Chapter 1. Characteristics of [entity from topic] with ### 1.1.–1.4.",
            methodology_instruction_pl="## Rozdział 2. Metodologia pracy z ### 2.1.–2.2.",
            methodology_instruction_en="## Chapter 2. Methodology with ### 2.1.–2.2.",
            results_instruction_pl=(
                "## Rozdział 3. Studium przypadku z ### 3.1.–3.3. "
                "(szczegółowy opis przypadku i procesu opieki)."
            ),
            results_instruction_en="## Chapter 3. Case study with ### 3.1.–3.3.",
            discussion_instruction_pl="",
            discussion_instruction_en="",
            conclusion_instruction_pl="# Zakończenie",
            conclusion_instruction_en="# Conclusion",
            appendix_instruction_pl="# Załączniki",
            appendix_instruction_en="# Appendices",
        )

    if tid == TEMPLATE_IMRAD:
        return ThesisTocSpec(
            template_id=tid,
            use_legacy_document_shell=False,
            skip_discussion_agent=False,
            empirical_placeholder_for_results=True,
            skeleton_outline_pl=_SKELETON_IMRAD_PL,
            skeleton_outline_en=_SKELETON_IMRAD_EN,
            numbering_instruction_pl=nb_pl,
            numbering_instruction_en=nb_en,
            intro_instruction_pl=(
                "Napisz **sekcje 1 i 2** w jednym fragmencie: "
                "## 1. Wstęp z ### 1.1. i ### 1.2.; następnie ## 2. Cel badań z ### 2.1. i ### 2.2."
            ),
            intro_instruction_en=(
                "Write **sections 1 and 2** together: "
                "## 1. Introduction with ### 1.1. and ### 1.2.; then ## 2. Aim with ### 2.1. and ### 2.2."
            ),
            lit_review_instruction_pl="",
            lit_review_instruction_en="",
            methodology_instruction_pl="## 3. Materiały i metody z ### 3.1.–3.3.",
            methodology_instruction_en="## 3. Materials and methods with ### 3.1.–3.3.",
            results_instruction_pl="## 4. Wyniki badań z ### 4.1., ### 4.2. …",
            results_instruction_en="## 4. Results with ### 4.1., ### 4.2. …",
            discussion_instruction_pl="## 5. Dyskusja",
            discussion_instruction_en="## 5. Discussion",
            conclusion_instruction_pl="## 6. Wnioski",
            conclusion_instruction_en="## 6. Conclusions",
            appendix_instruction_pl="## 7. Uzupełnienia (jeśli potrzebne)",
            appendix_instruction_en="## 7. Supplementary material (if needed)",
            references_heading_pl="Piśmiennictwo",
            references_heading_en="References",
        )

    # TEMPLATE_BUSINESS
    return ThesisTocSpec(
        template_id=tid,
        use_legacy_document_shell=False,
        skip_discussion_agent=True,
        empirical_placeholder_for_results=False,
        skeleton_outline_pl=_SKELETON_BUSINESS_PL,
        skeleton_outline_en=_SKELETON_BUSINESS_EN,
        numbering_instruction_pl=nb_pl,
        numbering_instruction_en=nb_en,
        intro_instruction_pl="# Wstęp",
        intro_instruction_en="# Introduction",
        lit_review_instruction_pl="## Rozdział I. [Podstawy teoretyczne] z ### 1.1.–1.3.",
        lit_review_instruction_en="## Chapter I. [Theoretical foundations] with ### 1.1.–1.3.",
        methodology_instruction_pl="## Rozdział II. Charakterystyka przedsiębiorstwa z ### 2.1.–2.3.",
        methodology_instruction_en="## Chapter II. Company profile with ### 2.1.–2.3.",
        results_instruction_pl="## Rozdział III. Analiza procesu/zjawiska z ### 3.1.–3.3.",
        results_instruction_en="## Chapter III. Process/phenomenon analysis with ### 3.1.–3.3.",
        discussion_instruction_pl="",
        discussion_instruction_en="",
        conclusion_instruction_pl="# Zakończenie",
        conclusion_instruction_en="# Conclusion",
        appendix_instruction_pl="",
        appendix_instruction_en="",
        references_heading_pl="Spis literatury",
        references_heading_en="List of references",
    )


def skeleton_for_language(spec: ThesisTocSpec, lang: str) -> str:
    base = (lang or "en").split("-")[0].lower()
    if base == "pl":
        return spec.skeleton_outline_pl
    return spec.skeleton_outline_en


def slot_instruction(spec: ThesisTocSpec, slot: str, lang: str) -> str:
    suf = "pl" if (lang or "en").split("-")[0].lower() == "pl" else "en"
    attr = f"{slot}_instruction_{suf}"
    return getattr(spec, attr, "") or ""


def formatter_user_input_suffix(spec: ThesisTocSpec, lang: str) -> str:
    base = (lang or "en").split("-")[0].lower()
    if base == "pl":
        num = spec.numbering_instruction_pl
    else:
        num = spec.numbering_instruction_en
    sk = skeleton_for_language(spec, lang)
    if not sk.strip():
        return f"\n\n{num}"
    return (
        f"\n\n**MANDATORY OUTLINE SKELETON** — preserve all sections; replace [brackets] with topic-specific titles:\n\n{sk}\n\n{num}"
    )


def literature_empirical_voice(
    slot: str,
    work_mode: str,
    lang: str,
) -> str:
    """Extra prompt fragment: anti-hallucination for literature vs empirical tone."""
    base = (lang or "en").split("-")[0].lower()
    pl = base == "pl"

    if work_mode == "literature_review":
        if slot in ("methodology", "results", "discussion"):
            if pl:
                return (
                    "\n\n**TRYB PRACY: PRZEGLĄD LITERATURY.** Nie twierdź, że przeprowadzono własne badania empiryczne. "
                    "Syntetyzuj metody i wyniki z cytowanej literatury; używaj zwrotów: „w literaturze…”, „badania {cite} wykazały…”. "
                    "Nie wymyślaj zbiorów danych ani procedur „my przeprowadziliśmy”."
                )
            return (
                "\n\n**WORK MODE: LITERATURE REVIEW.** Do not claim original empirical data collection. "
                "Synthesize methods and findings from cited sources; use phrasing like “prior research {cite} found…”. "
                "Do not invent datasets or write “we conducted” for new studies."
            )
        return ""

    # empirical
    if slot in ("methodology", "results", "discussion"):
        if pl:
            return (
                "\n\n**TRYB PRACY: STRUKTURA EMPIRYCZNA.** Pisz spójnie z rozdziałami metodologicznymi i wynikowymi pracy dyplomowej. "
                "Możesz opisać plan badania i ilustracyjne/schematyczne wyniki; unikaj sprzecznych stwierdzeń, że praca „nie jest empiryczna”. "
                "Nie twierdź o rzeczywistych danych autora, jeśli nie podano ich w kontekście — stosuj ostrożny, przykładowy język tam, gdzie potrzeba."
            )
        return (
            "\n\n**WORK MODE: EMPIRICAL STRUCTURE.** Write consistently with thesis chapters on methods and results. "
            "You may describe a study design and illustrative findings; do not contradict an empirical thesis structure. "
            "Do not claim real primary data from the author unless supplied in context — use cautious illustrative wording where needed."
        )
    return ""


def empirical_results_placeholder_markdown(spec: ThesisTocSpec, lang: str) -> str:
    base = (lang or "en").split("-")[0].lower()
    pl = base == "pl"
    if spec.template_id == TEMPLATE_CLASSIC_SOCIAL:
        if pl:
            body = (
                "## Rozdział IV. Analiza wyników badań własnych\n\n"
                "### 4.1. Charakterystyka grupy badawczej\n\n"
                "*[Zarezerwowane na wyniki badań własnych — uzupełnij w edytorze lub zaimportuj dane. "
                "Tu powinny znaleźć się opisy próby, tabela demograficzna itd.]*\n\n"
                "### 4.2. Wyniki badań (analiza danych)\n\n"
                "*[Miejsce na tabele, rysunki i interpretację własnych danych.]*\n\n"
                "### 4.3. Weryfikacja hipotez i wnioski\n\n"
                "*[Podsumowanie weryfikacji hipotez na podstawie własnych wyników.]*\n"
            )
        else:
            body = (
                "## Chapter IV. Analysis of own research results\n\n"
                "### 4.1. Study sample characteristics\n\n"
                "*[Reserved for own empirical results — complete in editor or import data.]*\n\n"
                "### 4.2. Results (data analysis)\n\n"
                "*[Place tables, figures, and interpretation of primary data here.]*\n\n"
                "### 4.3. Hypothesis verification and conclusions\n\n"
                "*[Summarize hypothesis testing based on own results.]*\n"
            )
        return body

    if spec.template_id == TEMPLATE_CASE_STUDY:
        if pl:
            return (
                "## Rozdział 3. Studium indywidualnego przypadku pacjenta\n\n"
                "### 3.1. Opis przypadku (wywiad, stan pacjenta)\n\n"
                "*[Zarezerwowane na dane kliniczne autora — uzupełnij w edytorze.]*\n\n"
                "### 3.2. Model opieki / proces pielęgnowania\n\n"
                "*[Diagnozy pielęgnowania, cele, interwencje — do uzupełnienia.]*\n\n"
                "### 3.3. Ocena uzyskanych wyników\n\n"
                "*[Do uzupełnienia po wprowadzeniu obserwacji.]*\n"
            )
        return (
            "## Chapter 3. Individual patient case study\n\n"
            "### 3.1. Case description\n\n"
            "*[Reserved for author-supplied clinical details.]*\n\n"
            "### 3.2. Care model / nursing process\n\n"
            "*[Nursing diagnoses, goals, interventions — to be completed.]*\n\n"
            "### 3.3. Outcome evaluation\n\n"
            "*[To be completed after observations.]*\n"
        )

    if spec.template_id == TEMPLATE_IMRAD:
        if pl:
            return (
                "## 4. Wyniki badań\n\n"
                "### 4.1.\n\n"
                "*[Zarezerwowane na wyniki własne — uzupełnij w edytorze.]*\n\n"
                "### 4.2.\n\n"
                "*[Kolejne zmienne / analizy — do uzupełnienia.]*\n"
            )
        return (
            "## 4. Results\n\n"
            "### 4.1.\n\n"
            "*[Reserved for own results — complete in editor.]*\n\n"
            "### 4.2.\n\n"
            "*[Further variables — to be completed.]*\n"
        )

    return ""


def should_skip_results_llm(
    spec: ThesisTocSpec,
    work_mode: str,
    user_results_markdown: Optional[str],
) -> bool:
    if user_results_markdown and str(user_results_markdown).strip():
        return False
    if work_mode != WORK_MODE_EMPIRICAL:
        return False
    return spec.empirical_placeholder_for_results


def caption_convention_fragment(lang: str) -> str:
    base = (lang or "en").split("-")[0].lower()
    pl = base == "pl"
    if pl:
        return (
            "\n\n**Podpisy do spisów:** Każdy rysunek: `![Rys. N. Pełny podpis](ścieżka)` z kolejnym N. "
            "Każda tabela: tuż pod tabelą osobna linia `: Tabela N. Pełny podpis` (składnia podpisu Pandoc)."
        )
    return (
        "\n\n**Captions for lists:** Each figure: `![Fig. N. Full caption](path)` with increasing N. "
        "Each table: immediately below the table, a line `: Table N. Full caption` (Pandoc caption syntax)."
    )


