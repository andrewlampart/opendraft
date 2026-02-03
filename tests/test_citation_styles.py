#!/usr/bin/env python3
"""
ABOUTME: Tests for citation style formatting
ABOUTME: Verifies APA and IEEE styles work correctly, and unsupported styles raise errors
"""

import pytest
import sys
from pathlib import Path

# Add engine to path
sys.path.insert(0, str(Path(__file__).parent.parent / "engine"))

from utils.citation_database import Citation, CitationDatabase
from utils.citation_compiler import CitationCompiler


# =============================================================================
# TEST FIXTURES
# =============================================================================

@pytest.fixture
def sample_citation_single_author():
    """Single author citation for testing."""
    return Citation(
        citation_id="cite_001",
        authors=["Smith"],
        year=2023,
        title="Machine Learning Applications",
        source_type="journal",
        journal="Nature",
        volume=45,
        issue=3,
        pages="123-145",
        doi="10.1234/nature.2023.001"
    )


@pytest.fixture
def sample_citation_two_authors():
    """Two author citation for testing."""
    return Citation(
        citation_id="cite_002",
        authors=["Smith", "Johnson"],
        year=2022,
        title="Deep Learning Methods",
        source_type="journal",
        journal="Science",
        volume=30,
        pages="50-75"
    )


@pytest.fixture
def sample_citation_multiple_authors():
    """Multiple (3+) author citation for testing."""
    return Citation(
        citation_id="cite_003",
        authors=["Smith", "Johnson", "Williams", "Brown"],
        year=2021,
        title="AI in Healthcare",
        source_type="book",
        publisher="Academic Press"
    )


@pytest.fixture
def apa_database():
    """Database configured for APA style."""
    return CitationDatabase(citations=[], citation_style="APA 7th")


@pytest.fixture
def ieee_database():
    """Database configured for IEEE style."""
    return CitationDatabase(citations=[], citation_style="IEEE")


# =============================================================================
# APA IN-TEXT CITATION TESTS
# =============================================================================

class TestAPAInTextCitations:
    """Test APA 7th edition in-text citation formatting."""

    def test_single_author(self, apa_database, sample_citation_single_author):
        """Single author: (Smith, 2023)"""
        compiler = CitationCompiler(apa_database)
        result = compiler.format_in_text_citation(sample_citation_single_author)
        assert result == "(Smith, 2023)"

    def test_two_authors(self, apa_database, sample_citation_two_authors):
        """Two authors: (Smith & Johnson, 2022)"""
        compiler = CitationCompiler(apa_database)
        result = compiler.format_in_text_citation(sample_citation_two_authors)
        assert result == "(Smith & Johnson, 2022)"

    def test_multiple_authors(self, apa_database, sample_citation_multiple_authors):
        """3+ authors: (Smith et al., 2021)"""
        compiler = CitationCompiler(apa_database)
        result = compiler.format_in_text_citation(sample_citation_multiple_authors)
        assert result == "(Smith et al., 2021)"


# =============================================================================
# IEEE IN-TEXT CITATION TESTS
# =============================================================================

class TestIEEEInTextCitations:
    """Test IEEE numbered citation formatting."""

    def test_numbered_format(self, ieee_database, sample_citation_single_author):
        """IEEE uses numbered format: [1]"""
        compiler = CitationCompiler(ieee_database)
        result = compiler.format_in_text_citation(sample_citation_single_author)
        assert result == "[1]"

    def test_numbered_format_double_digit(self, ieee_database):
        """IEEE with double digit: [12]"""
        citation = Citation(
            citation_id="cite_012",
            authors=["Test"],
            year=2023,
            title="Test Paper",
            source_type="journal"
        )
        compiler = CitationCompiler(ieee_database)
        result = compiler.format_in_text_citation(citation)
        assert result == "[12]"


# =============================================================================
# APA REFERENCE FORMATTING TESTS
# =============================================================================

class TestAPAReferenceFormatting:
    """Test APA 7th edition reference list formatting."""

    def test_journal_article(self, apa_database, sample_citation_single_author):
        """Journal article with DOI."""
        compiler = CitationCompiler(apa_database)
        result = compiler._format_apa_reference(sample_citation_single_author)

        assert "Smith." in result
        assert "(2023)" in result
        assert "Machine Learning Applications" in result
        assert "*Nature*" in result
        assert "https://doi.org/10.1234/nature.2023.001" in result

    def test_book(self, apa_database, sample_citation_multiple_authors):
        """Book with publisher."""
        compiler = CitationCompiler(apa_database)
        result = compiler._format_apa_reference(sample_citation_multiple_authors)

        assert "Smith" in result
        assert "(2021)" in result
        assert "*AI in Healthcare*" in result
        assert "Academic Press" in result


# =============================================================================
# UNSUPPORTED STYLE TESTS
# =============================================================================

class TestUnsupportedStyles:
    """Test that unsupported styles raise appropriate errors."""

    def test_chicago_raises_error(self, sample_citation_single_author):
        """Chicago style should raise NotImplementedError."""
        db = CitationDatabase(citations=[], citation_style="Chicago")
        compiler = CitationCompiler(db)

        with pytest.raises(NotImplementedError) as exc_info:
            compiler.format_in_text_citation(sample_citation_single_author)

        assert "Chicago" in str(exc_info.value)
        assert "not yet implemented" in str(exc_info.value)

    def test_mla_raises_error(self, sample_citation_single_author):
        """MLA style should raise NotImplementedError."""
        db = CitationDatabase(citations=[], citation_style="MLA")
        compiler = CitationCompiler(db)

        with pytest.raises(NotImplementedError) as exc_info:
            compiler.format_in_text_citation(sample_citation_single_author)

        assert "MLA" in str(exc_info.value)
        assert "not yet implemented" in str(exc_info.value)

    def test_unknown_style_raises_error(self, sample_citation_single_author):
        """Unknown style should raise NotImplementedError."""
        db = CitationDatabase(citations=[], citation_style="Harvard")
        compiler = CitationCompiler(db)

        with pytest.raises(NotImplementedError) as exc_info:
            compiler.format_in_text_citation(sample_citation_single_author)

        assert "Harvard" in str(exc_info.value)


# =============================================================================
# REFERENCE LIST GENERATION TESTS
# =============================================================================

class TestReferenceListGeneration:
    """Test full reference list generation."""

    def test_apa_reference_list_sorted(self, apa_database):
        """APA references should be sorted alphabetically by first author."""
        citations = [
            Citation(citation_id="cite_001", authors=["Zebra"], year=2023, title="Z Paper", source_type="journal"),
            Citation(citation_id="cite_002", authors=["Alpha"], year=2022, title="A Paper", source_type="journal"),
            Citation(citation_id="cite_003", authors=["Middle"], year=2021, title="M Paper", source_type="journal"),
        ]
        db = CitationDatabase(citations=citations, citation_style="APA 7th")
        compiler = CitationCompiler(db)

        # Create text with all citations
        text = "Test {cite_001} and {cite_002} and {cite_003}"
        result = compiler.generate_reference_list(text)

        # Alpha should come before Middle, Middle before Zebra
        alpha_pos = result.find("Alpha")
        middle_pos = result.find("Middle")
        zebra_pos = result.find("Zebra")

        assert alpha_pos < middle_pos < zebra_pos


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
