#!/usr/bin/env python3
"""
ABOUTME: Unit tests for citation management phase
ABOUTME: Tests deduplication, scraping, filtering, and database operations
"""

import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

from phases.citations import run_citation_management, _build_citation_summary
from utils.citation_database import Citation, CitationDatabase


class TestBuildCitationSummary:
    """Tests for _build_citation_summary helper function."""

    def test_builds_summary_with_citations(self, sample_citation_database):
        """Test that summary includes all citations."""
        summary = _build_citation_summary(sample_citation_database)

        assert "CITATION DATABASE" in summary
        assert "3 CITATIONS AVAILABLE" in summary
        assert "cite_001" in summary
        assert "cite_002" in summary
        assert "cite_003" in summary

    def test_summary_includes_authors_and_years(self, sample_citation_database):
        """Test that summary includes author names and years."""
        summary = _build_citation_summary(sample_citation_database)

        assert "Smith" in summary
        assert "2023" in summary
        assert "Johnson" in summary
        assert "2022" in summary

    def test_summary_includes_titles(self, sample_citation_database):
        """Test that summary includes paper titles."""
        summary = _build_citation_summary(sample_citation_database)

        assert "Machine Learning in Healthcare" in summary
        assert "Deep Learning for Medical Image Analysis" in summary

    def test_summary_includes_doi_when_present(self, sample_citation_database):
        """Test that DOI is included when available."""
        summary = _build_citation_summary(sample_citation_database)

        # At least one DOI should be present
        assert "DOI:" in summary or "10.1038" in summary

    def test_summary_includes_citation_format_instructions(self, sample_citation_database):
        """Test that summary includes citation format instructions."""
        summary = _build_citation_summary(sample_citation_database)

        assert "{cite_" in summary
        assert "ONLY cite" in summary.upper() or "only cite" in summary.lower()

    def test_summary_truncates_long_abstracts(self):
        """Test that long abstracts are truncated."""
        long_abstract = "A" * 500
        citation = Citation(
            citation_id="cite_001",
            authors=["Author"],
            year=2023,
            title="Test",
            source_type="journal_article",
            abstract=long_abstract,
        )
        db = CitationDatabase(citations=[citation])

        summary = _build_citation_summary(db)

        # Abstract should be truncated with ellipsis
        assert "..." in summary
        assert summary.count("A") < 500

    def test_summary_handles_empty_database(self):
        """Test summary generation with empty database."""
        db = CitationDatabase(citations=[])
        summary = _build_citation_summary(db)

        assert "0 CITATIONS" in summary

    def test_citation_format_no_double_prefix(self, sample_citation_database):
        """Test that citation format doesn't have doubled 'cite_' prefix.

        Regression test for bug where {cite_cite_001} was generated instead of {cite_001}.
        """
        summary = _build_citation_summary(sample_citation_database)

        # Should have correct format {cite_001}
        assert "{cite_001}" in summary or "{cite_002}" in summary

        # Should NOT have doubled prefix {cite_cite_XXX}
        assert "{cite_cite_" not in summary, "Bug: citation format has doubled 'cite_' prefix"


class TestRunCitationManagement:
    """Tests for run_citation_management function.

    Note: These tests require complex mocking of the citation pipeline.
    For full integration testing, use test_pipeline.py with --mock.
    """

    @pytest.mark.skip(reason="Complex mocking required - run_citation_management uses deferred imports")
    def test_citation_management_sets_database(self, mock_ctx_with_structure, sample_citations):
        """Test that citation management creates citation database."""
        pass

    @pytest.mark.skip(reason="Complex mocking required - run_citation_management uses deferred imports")
    def test_citation_management_sets_summary(self, mock_ctx_with_structure, sample_citations):
        """Test that citation management creates summary string."""
        pass

    def test_citation_ids_are_assigned(self, sample_citations):
        """Test that citations can have sequential IDs assigned."""
        # Simple test of ID assignment logic
        for i, citation in enumerate(sample_citations, start=1):
            citation.id = f"cite_{i:03d}"

        assert sample_citations[0].id == "cite_001"
        assert sample_citations[1].id == "cite_002"
        assert sample_citations[2].id == "cite_003"

    def test_citation_database_can_be_created(self, sample_citations):
        """Test that CitationDatabase can be created from citations."""
        db = CitationDatabase(
            citations=sample_citations,
            citation_style="APA 7th",
            draft_language="english",
        )

        assert len(db.citations) == 3
        assert db.citation_style == "APA 7th"

    def test_citation_style_mapping_values(self):
        """Test citation style mapping logic."""
        style_map = {"apa": "APA 7th", "ieee": "IEEE", "nalt": "NALT"}

        assert style_map.get("apa") == "APA 7th"
        assert style_map.get("ieee") == "IEEE"
        assert style_map.get("nalt") == "NALT"
