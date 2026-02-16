#!/usr/bin/env python3
"""
ABOUTME: Unit tests for research phase
ABOUTME: Tests Scout, Scribe, Signal agents and helper functions
"""

import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

from phases.research import run_research_phase, split_scribe_to_papers, _slugify


class TestSlugify:
    """Tests for _slugify helper function."""

    def test_basic_slugify(self):
        """Test basic text to slug conversion."""
        assert _slugify("Hello World") == "hello_world"

    def test_slugify_removes_special_chars(self):
        """Test that special characters are removed."""
        assert _slugify("Hello! World?") == "hello_world"

    def test_slugify_respects_max_length(self):
        """Test max_length parameter."""
        result = _slugify("This is a very long title that should be truncated", max_length=10)
        assert len(result) <= 10

    def test_slugify_handles_empty_string(self):
        """Test empty string handling."""
        assert _slugify("") == ""


class TestSplitScribeToPapers:
    """Tests for split_scribe_to_papers function."""

    def test_splits_numbered_papers(self, temp_output_dir):
        """Test splitting scribe output with numbered paper format."""
        scribe_output = """
## Paper 1: Machine Learning Applications
**Authors:** Smith, J.
**Year:** 2023
Content of first paper.

## Paper 2: Deep Learning Review
**Authors:** Jones, A.
**Year:** 2022
Content of second paper.
"""
        papers_dir = temp_output_dir['papers']
        created = split_scribe_to_papers(scribe_output, papers_dir, verbose=False)

        assert len(created) == 2
        assert all(f.exists() for f in created)
        assert all(f.suffix == ".md" for f in created)

    def test_handles_no_papers(self, temp_output_dir):
        """Test handling when no papers can be parsed."""
        scribe_output = "Just some random text without paper structure."
        papers_dir = temp_output_dir['papers']

        created = split_scribe_to_papers(scribe_output, papers_dir, verbose=False)
        assert created == []

    def test_extracts_metadata(self, temp_output_dir):
        """Test that year and author are extracted for filenames."""
        scribe_output = """
## Paper 1: Test Paper Title
**Authors:** Johnson, Mary
**Year:** 2024
Paper content here.
"""
        papers_dir = temp_output_dir['papers']
        created = split_scribe_to_papers(scribe_output, papers_dir, verbose=False)

        assert len(created) == 1
        filename = created[0].name
        assert "johnson" in filename.lower()
        assert "2024" in filename


class TestRunResearchPhase:
    """Tests for run_research_phase function."""

    def test_research_phase_sets_outputs(self, mock_ctx):
        """Test that research phase sets expected context outputs."""
        # Mock the research_citations_via_api function
        mock_citations = [MagicMock(
            title="Test Paper",
            authors=["Author A"],
            year=2023,
            api_source="crossref",
        )]

        with patch('phases.research.research_citations_via_api') as mock_research:
            mock_research.return_value = {
                'count': 1,
                'citations': mock_citations,
            }

            with patch('phases.research.run_agent') as mock_run_agent:
                mock_run_agent.return_value = "Mocked agent output"

                with patch('phases.research.rate_limit_delay'):
                    # Write scout file so it can be read
                    scout_path = mock_ctx.folders['research'] / "scout_raw.md"
                    scout_path.write_text("## Scout Results\n\n#### 1. Paper\n**Authors**: Test", encoding='utf-8')

                    run_research_phase(mock_ctx)

        # Verify outputs were set
        assert mock_ctx.scout_result is not None
        assert mock_ctx.scout_result['count'] == 1
        assert mock_ctx.scribe_output == "Mocked agent output"
        assert mock_ctx.signal_output == "Mocked agent output"

    def test_research_phase_raises_on_insufficient_citations(self, mock_ctx):
        """Test that research phase raises ValueError on insufficient citations."""
        with patch('phases.research.research_citations_via_api') as mock_research:
            mock_research.side_effect = ValueError("Insufficient citations")

            with pytest.raises(ValueError) as exc_info:
                run_research_phase(mock_ctx)

            assert "Insufficient citations" in str(exc_info.value)

    def test_research_phase_calls_agents_in_order(self, mock_ctx):
        """Test that Scribe and Signal agents are called after Scout."""
        mock_citations = [MagicMock(
            title="Test",
            authors=["A"],
            year=2023,
            api_source="crossref",
        )]

        call_order = []

        def track_agent_calls(**kwargs):
            call_order.append(kwargs.get('name', ''))
            return "output"

        with patch('phases.research.research_citations_via_api') as mock_research:
            mock_research.return_value = {'count': 1, 'citations': mock_citations}

            with patch('phases.research.run_agent', side_effect=track_agent_calls):
                with patch('phases.research.rate_limit_delay'):
                    scout_path = mock_ctx.folders['research'] / "scout_raw.md"
                    scout_path.write_text("## Scout\n\n#### 1. Paper\n**Authors**: Test", encoding='utf-8')

                    run_research_phase(mock_ctx)

        assert len(call_order) == 2
        assert "Scribe" in call_order[0]
        assert "Signal" in call_order[1]
