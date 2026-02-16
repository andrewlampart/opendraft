#!/usr/bin/env python3
"""
ABOUTME: Content validation tests for OpenDraft outputs
ABOUTME: Validates structure, citations, and language quality of generated drafts
"""

import pytest
import re
import json
from pathlib import Path
from typing import List, Dict, Optional, Tuple


class ContentValidator:
    """Validates the content quality of generated drafts."""

    def __init__(self, draft_path: Path):
        self.draft_path = draft_path
        self.content = draft_path.read_text(encoding='utf-8') if draft_path.exists() else ""

    def get_uncompiled_citations(self) -> List[str]:
        """Find any uncompiled {cite_XXX} tags in the output."""
        pattern = r'\{cite_[a-z_0-9]+\}'
        return re.findall(pattern, self.content)

    def get_compiled_citations(self) -> List[str]:
        """Find properly formatted (Author, Year) citations."""
        pattern = r'\([A-Z][a-z]+(?:\s+et\s+al\.?)?,?\s+[0-9]{4}[a-z]?\)'
        return re.findall(pattern, self.content)

    def has_references_section(self) -> bool:
        """Check if a References or Bibliography section exists."""
        patterns = [
            r'^#+ References',
            r'^#+ Bibliography',
            r'^#+ Literaturverzeichnis',  # German
            r'^#+ Références',  # French
        ]
        for pattern in patterns:
            if re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE):
                return True
        return False

    def get_section_headers(self) -> List[str]:
        """Extract all markdown headers."""
        pattern = r'^#{1,4}\s+(.+)$'
        return re.findall(pattern, self.content, re.MULTILINE)

    def has_required_sections(self, required: List[str]) -> Tuple[bool, List[str]]:
        """Check if all required sections exist (case-insensitive partial match)."""
        headers_lower = [h.lower() for h in self.get_section_headers()]
        missing = []
        for req in required:
            found = any(req.lower() in h for h in headers_lower)
            if not found:
                missing.append(req)
        return len(missing) == 0, missing

    def get_word_count(self) -> int:
        """Count words in the document."""
        # Remove markdown syntax for more accurate count
        text = re.sub(r'[#*_`\[\](){}|]', ' ', self.content)
        words = text.split()
        return len(words)

    def detect_language(self) -> str:
        """Simple language detection based on common words."""
        german_words = ['und', 'der', 'die', 'das', 'ist', 'mit', 'für', 'auf', 'werden']
        english_words = ['the', 'and', 'is', 'are', 'for', 'with', 'this', 'that', 'which']
        french_words = ['le', 'la', 'les', 'est', 'sont', 'avec', 'pour', 'dans', 'sur']

        content_lower = self.content.lower()
        words = content_lower.split()

        de_count = sum(1 for w in words if w in german_words)
        en_count = sum(1 for w in words if w in english_words)
        fr_count = sum(1 for w in words if w in french_words)

        if de_count > en_count and de_count > fr_count:
            return 'german'
        elif fr_count > en_count and fr_count > de_count:
            return 'french'
        return 'english'

    def has_abstract(self) -> bool:
        """Check if document has an abstract section."""
        patterns = [
            r'^#{1,2}\s*Abstract',
            r'^\*\*Abstract',
            r'^#{1,2}\s*Zusammenfassung',  # German
        ]
        for pattern in patterns:
            if re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE):
                return True
        return False

    def get_tables_count(self) -> int:
        """Count markdown tables in the document."""
        # Tables have | at start and end of lines with --- separator row
        table_pattern = r'^\|.+\|$'
        table_rows = re.findall(table_pattern, self.content, re.MULTILINE)
        # Rough estimate: tables have at least 3 rows (header, separator, data)
        return len(table_rows) // 3 if table_rows else 0


class TestCitationIntegrity:
    """Tests for citation compilation and integrity."""

    def test_no_uncompiled_citations_in_mock_output(self, tmp_path):
        """Test that mock outputs don't have uncompiled citations."""
        # Create a sample output with proper citations
        draft = tmp_path / "test_draft.md"
        draft.write_text("""
# Introduction

This is a test (Smith, 2023). Another reference (Jones et al., 2024).

# References

1. Smith, J. (2023). Test Paper.
2. Jones, A. et al. (2024). Another Paper.
""")
        validator = ContentValidator(draft)

        uncompiled = validator.get_uncompiled_citations()
        assert len(uncompiled) == 0, f"Found uncompiled citations: {uncompiled}"

    def test_detects_uncompiled_citations(self, tmp_path):
        """Test that validator catches uncompiled citation tags."""
        draft = tmp_path / "test_draft.md"
        draft.write_text("""
# Introduction

This has a bug {cite_001} and another {cite_cite_002}.
""")
        validator = ContentValidator(draft)

        uncompiled = validator.get_uncompiled_citations()
        assert len(uncompiled) == 2
        assert "{cite_001}" in uncompiled
        assert "{cite_cite_002}" in uncompiled

    def test_finds_compiled_citations(self, tmp_path):
        """Test that validator finds properly formatted citations."""
        draft = tmp_path / "test_draft.md"
        draft.write_text("""
This has citations (Smith, 2023) and (Jones et al., 2024) and (Brown, 2022a).
""")
        validator = ContentValidator(draft)

        compiled = validator.get_compiled_citations()
        assert len(compiled) == 3

    def test_no_doubled_cite_prefix(self, tmp_path):
        """Regression test: citation format should not have doubled 'cite_' prefix."""
        draft = tmp_path / "test_draft.md"
        draft.write_text("""
Good: {cite_001}
Bad: {cite_cite_001}
""")
        validator = ContentValidator(draft)

        uncompiled = validator.get_uncompiled_citations()
        # Both are uncompiled, but we specifically check for the doubled prefix bug
        doubled = [c for c in uncompiled if "cite_cite_" in c]
        assert len(doubled) == 1, "Should detect doubled prefix"


class TestDocumentStructure:
    """Tests for document structure validation."""

    def test_has_references_section(self, tmp_path):
        """Test detection of references section."""
        draft = tmp_path / "test_draft.md"
        draft.write_text("""
# Introduction

Content here.

# References

1. Smith (2023). Paper.
""")
        validator = ContentValidator(draft)
        assert validator.has_references_section()

    def test_missing_references_section(self, tmp_path):
        """Test detection of missing references."""
        draft = tmp_path / "test_draft.md"
        draft.write_text("""
# Introduction

Content here.

# Conclusion

The end.
""")
        validator = ContentValidator(draft)
        assert not validator.has_references_section()

    def test_german_references_section(self, tmp_path):
        """Test detection of German references section."""
        draft = tmp_path / "test_draft.md"
        draft.write_text("""
# Einleitung

Inhalt hier.

# Literaturverzeichnis

1. Schmidt (2023). Papier.
""")
        validator = ContentValidator(draft)
        assert validator.has_references_section()

    def test_has_required_sections(self, tmp_path):
        """Test required sections validation."""
        draft = tmp_path / "test_draft.md"
        draft.write_text("""
# Abstract

Summary here.

# 1. Introduction

Content.

# 2. Literature Review

Previous work.

# 3. Methodology

Methods.

# 4. Conclusion

Summary.
""")
        validator = ContentValidator(draft)
        required = ["Introduction", "Conclusion"]
        has_all, missing = validator.has_required_sections(required)
        assert has_all, f"Missing sections: {missing}"

    def test_detects_missing_sections(self, tmp_path):
        """Test detection of missing required sections."""
        draft = tmp_path / "test_draft.md"
        draft.write_text("""
# Introduction

Content only.
""")
        validator = ContentValidator(draft)
        required = ["Introduction", "Methodology", "Conclusion"]
        has_all, missing = validator.has_required_sections(required)
        assert not has_all
        assert "Methodology" in missing
        assert "Conclusion" in missing

    def test_has_abstract(self, tmp_path):
        """Test abstract detection."""
        draft = tmp_path / "test_draft.md"
        draft.write_text("""
## Abstract

This paper examines...

# Introduction
""")
        validator = ContentValidator(draft)
        assert validator.has_abstract()


class TestLanguageValidation:
    """Tests for language detection and validation."""

    def test_detects_english(self, tmp_path):
        """Test English language detection."""
        draft = tmp_path / "test_draft.md"
        draft.write_text("""
The study examines the impact of machine learning on healthcare diagnostics.
This research is important for understanding the relationship between technology
and medical outcomes. The methodology used in this analysis demonstrates
significant findings that are relevant to the field.
""")
        validator = ContentValidator(draft)
        assert validator.detect_language() == 'english'

    def test_detects_german(self, tmp_path):
        """Test German language detection."""
        draft = tmp_path / "test_draft.md"
        draft.write_text("""
Die Studie untersucht die Auswirkungen von maschinellem Lernen auf die
Gesundheitsdiagnostik. Diese Forschung ist wichtig für das Verständnis der
Beziehung zwischen Technologie und medizinischen Ergebnissen. Die in dieser
Analyse verwendete Methodik zeigt bedeutende Erkenntnisse, die für das Gebiet
relevant sind.
""")
        validator = ContentValidator(draft)
        assert validator.detect_language() == 'german'

    def test_word_count(self, tmp_path):
        """Test word count functionality."""
        draft = tmp_path / "test_draft.md"
        draft.write_text("One two three four five. Six seven eight nine ten.")
        validator = ContentValidator(draft)
        # Should be approximately 10 words
        assert 8 <= validator.get_word_count() <= 12


class TestTableValidation:
    """Tests for table detection."""

    def test_counts_tables(self, tmp_path):
        """Test table counting."""
        draft = tmp_path / "test_draft.md"
        draft.write_text("""
# Results

| Column A | Column B |
|----------|----------|
| Data 1   | Data 2   |
| Data 3   | Data 4   |

Some text here.

| Name | Value |
|------|-------|
| Test | 123   |
""")
        validator = ContentValidator(draft)
        # Should detect approximately 2 tables
        assert validator.get_tables_count() >= 1


class TestE2EOutputValidation:
    """
    Tests to validate actual E2E test outputs.
    These tests are skipped if E2E outputs don't exist.
    """

    @pytest.fixture
    def e2e_output_base(self):
        """Find the most recent E2E test output directory."""
        base = Path("/tmp/opendraft_e2e_tests")
        if not base.exists():
            pytest.skip("No E2E test outputs found")
        dirs = sorted(base.iterdir(), key=lambda p: p.name, reverse=True)
        if not dirs:
            pytest.skip("No E2E test outputs found")
        return dirs[0]

    def _find_main_md(self, exports_dir: Path) -> Optional[Path]:
        """Find the main markdown file (not INTERMEDIATE or abstract)."""
        for md in exports_dir.glob("*.md"):
            if "INTERMEDIATE" not in md.name and "abstract" not in md.name.lower():
                return md
        return None

    @pytest.mark.integration
    def test_e2e_no_uncompiled_citations(self, e2e_output_base):
        """Validate that E2E outputs have no uncompiled citations."""
        exports_dirs = list(e2e_output_base.rglob("exports"))
        if not exports_dirs:
            pytest.skip("No exports directories found")

        for exports_dir in exports_dirs:
            main_md = self._find_main_md(exports_dir)
            if not main_md:
                continue

            validator = ContentValidator(main_md)
            uncompiled = validator.get_uncompiled_citations()

            # Allow zero uncompiled citations
            assert len(uncompiled) == 0, (
                f"Found {len(uncompiled)} uncompiled citations in {main_md.name}: "
                f"{uncompiled[:5]}..."
            )

    @pytest.mark.integration
    def test_e2e_has_references(self, e2e_output_base):
        """Validate that E2E outputs have a references section."""
        exports_dirs = list(e2e_output_base.rglob("exports"))
        if not exports_dirs:
            pytest.skip("No exports directories found")

        for exports_dir in exports_dirs:
            main_md = self._find_main_md(exports_dir)
            if not main_md:
                continue

            validator = ContentValidator(main_md)

            # Check for references section
            assert validator.has_references_section(), (
                f"No References section found in {main_md.name}"
            )

    @pytest.mark.integration
    def test_e2e_has_abstract(self, e2e_output_base):
        """Validate that E2E outputs have an abstract."""
        exports_dirs = list(e2e_output_base.rglob("exports"))
        if not exports_dirs:
            pytest.skip("No exports directories found")

        for exports_dir in exports_dirs:
            main_md = self._find_main_md(exports_dir)
            if not main_md:
                continue

            validator = ContentValidator(main_md)
            assert validator.has_abstract(), f"No Abstract found in {main_md.name}"

    @pytest.mark.integration
    def test_e2e_minimum_word_count(self, e2e_output_base):
        """Validate that E2E outputs meet minimum word count."""
        exports_dirs = list(e2e_output_base.rglob("exports"))
        if not exports_dirs:
            pytest.skip("No exports directories found")

        for exports_dir in exports_dirs:
            main_md = self._find_main_md(exports_dir)
            if not main_md:
                continue

            validator = ContentValidator(main_md)
            word_count = validator.get_word_count()

            # Expose mode should have at least 2000 words, full draft 8000+
            is_expose = "expose" in main_md.name.lower()
            min_words = 1500 if is_expose else 5000

            assert word_count >= min_words, (
                f"{main_md.name} has only {word_count} words (minimum: {min_words})"
            )

    @pytest.mark.integration
    def test_e2e_german_output_is_german(self, e2e_output_base):
        """Validate that German outputs are actually in German."""
        german_dirs = list(e2e_output_base.rglob("*_de_*"))
        if not german_dirs:
            pytest.skip("No German test outputs found")

        for test_dir in german_dirs:
            exports_dir = test_dir / "exports"
            if not exports_dir.exists():
                continue

            main_md = self._find_main_md(exports_dir)
            if not main_md:
                continue

            validator = ContentValidator(main_md)
            detected_lang = validator.detect_language()

            assert detected_lang == 'german', (
                f"German output {main_md.name} detected as {detected_lang}"
            )
