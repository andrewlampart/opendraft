#!/usr/bin/env python3
"""
ABOUTME: Unit tests for compose phase
ABOUTME: Tests 7 Crafter agents writing thesis sections
"""

import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock, call

from phases.compose import (
    run_compose_phase,
    _write_introduction,
    _write_literature_review,
    _write_methodology,
    _write_results,
    _write_discussion,
    _merge_body_sections,
    _write_conclusion,
    _write_appendices,
)


class TestWriteIntroduction:
    """Tests for _write_introduction helper."""

    def test_sets_intro_output(self, mock_ctx_with_citations):
        """Test that introduction output is set on context."""
        with patch('phases.compose.run_agent', return_value="# Introduction\n\nContent"):
            _write_introduction(mock_ctx_with_citations)

        assert mock_ctx_with_citations.intro_output != ""
        assert "Introduction" in mock_ctx_with_citations.intro_output

    def test_saves_to_file(self, mock_ctx_with_citations):
        """Test that introduction is saved to correct file."""
        saved_path = None

        def capture_save(model, name, save_to, **kwargs):
            nonlocal saved_path
            saved_path = save_to
            return "# Introduction"

        with patch('phases.compose.run_agent', side_effect=capture_save):
            _write_introduction(mock_ctx_with_citations)

        assert saved_path is not None
        assert "01_introduction" in str(saved_path)

    def test_includes_word_target(self, mock_ctx_with_citations):
        """Test that word target is included in prompt."""
        captured_input = None

        def capture_input(model, name, user_input, **kwargs):
            nonlocal captured_input
            captured_input = user_input
            return "# Introduction"

        with patch('phases.compose.run_agent', side_effect=capture_input):
            _write_introduction(mock_ctx_with_citations)

        assert captured_input is not None
        assert mock_ctx_with_citations.word_targets['introduction'] in captured_input


class TestWriteLiteratureReview:
    """Tests for _write_literature_review helper."""

    def test_sets_lit_review_output(self, mock_ctx_with_citations):
        """Test that literature review output is set."""
        with patch('phases.compose.run_agent', return_value="## 2.1 Literature Review\n\nContent"):
            _write_literature_review(mock_ctx_with_citations)

        assert mock_ctx_with_citations.lit_review_output != ""
        assert "Literature Review" in mock_ctx_with_citations.lit_review_output

    def test_uses_scribe_output(self, mock_ctx_with_citations):
        """Test that scribe output is included in prompt."""
        captured_input = None

        def capture_input(model, name, user_input, **kwargs):
            nonlocal captured_input
            captured_input = user_input
            return "## 2.1 Lit Review"

        mock_ctx_with_citations.scribe_output = "UNIQUE_SCRIBE_CONTENT_XYZ"

        with patch('phases.compose.run_agent', side_effect=capture_input):
            _write_literature_review(mock_ctx_with_citations)

        assert "UNIQUE_SCRIBE_CONTENT_XYZ" in captured_input


class TestWriteMethodology:
    """Tests for _write_methodology helper."""

    def test_sets_methodology_output(self, mock_ctx_with_citations):
        """Test that methodology output is set."""
        mock_ctx_with_citations.lit_review_output = "Previous lit review content"

        with patch('phases.compose.run_agent', return_value="## 2.2 Methodology"):
            _write_methodology(mock_ctx_with_citations)

        assert mock_ctx_with_citations.methodology_output != ""

    def test_references_lit_review(self, mock_ctx_with_citations):
        """Test that methodology prompt references literature review."""
        captured_input = None

        def capture_input(model, name, user_input, **kwargs):
            nonlocal captured_input
            captured_input = user_input
            return "## 2.2 Methodology"

        mock_ctx_with_citations.lit_review_output = "UNIQUE_LIT_REVIEW_ABC"

        with patch('phases.compose.run_agent', side_effect=capture_input):
            _write_methodology(mock_ctx_with_citations)

        assert "UNIQUE_LIT_REVIEW_ABC" in captured_input


class TestWriteResults:
    """Tests for _write_results helper."""

    def test_sets_results_output(self, mock_ctx_with_citations):
        """Test that results output is set."""
        mock_ctx_with_citations.lit_review_output = "Lit review"
        mock_ctx_with_citations.methodology_output = "Methodology content"

        with patch('phases.compose.run_agent', return_value="## 2.3 Results"):
            _write_results(mock_ctx_with_citations)

        assert mock_ctx_with_citations.results_output != ""


class TestWriteDiscussion:
    """Tests for _write_discussion helper."""

    def test_sets_discussion_output(self, mock_ctx_with_citations):
        """Test that discussion output is set."""
        mock_ctx_with_citations.lit_review_output = "Lit review"
        mock_ctx_with_citations.results_output = "Results content"

        with patch('phases.compose.run_agent', return_value="## 2.4 Discussion"):
            _write_discussion(mock_ctx_with_citations)

        assert mock_ctx_with_citations.discussion_output != ""

    def test_references_results(self, mock_ctx_with_citations):
        """Test that discussion prompt references results."""
        captured_input = None

        def capture_input(model, name, user_input, **kwargs):
            nonlocal captured_input
            captured_input = user_input
            return "## 2.4 Discussion"

        mock_ctx_with_citations.results_output = "UNIQUE_RESULTS_789"
        mock_ctx_with_citations.lit_review_output = "Lit review"

        with patch('phases.compose.run_agent', side_effect=capture_input):
            _write_discussion(mock_ctx_with_citations)

        assert "UNIQUE_RESULTS_789" in captured_input


class TestMergeBodySections:
    """Tests for _merge_body_sections helper."""

    def test_merges_all_sections(self, mock_ctx_with_citations):
        """Test that all body sections are merged."""
        # Write section files
        drafts_dir = mock_ctx_with_citations.folders['drafts']
        (drafts_dir / "02_1_literature_review.md").write_text("Lit review content", encoding='utf-8')
        (drafts_dir / "02_2_methodology.md").write_text("Methodology content", encoding='utf-8')
        (drafts_dir / "02_3_analysis_results.md").write_text("Results content", encoding='utf-8')
        (drafts_dir / "02_4_discussion.md").write_text("Discussion content", encoding='utf-8')

        _merge_body_sections(mock_ctx_with_citations)

        assert "Lit review content" in mock_ctx_with_citations.body_output
        assert "Methodology content" in mock_ctx_with_citations.body_output
        assert "Results content" in mock_ctx_with_citations.body_output
        assert "Discussion content" in mock_ctx_with_citations.body_output

    def test_creates_merged_file(self, mock_ctx_with_citations):
        """Test that merged file is created."""
        drafts_dir = mock_ctx_with_citations.folders['drafts']
        (drafts_dir / "02_1_literature_review.md").write_text("Content", encoding='utf-8')
        (drafts_dir / "02_2_methodology.md").write_text("Content", encoding='utf-8')
        (drafts_dir / "02_3_analysis_results.md").write_text("Content", encoding='utf-8')
        (drafts_dir / "02_4_discussion.md").write_text("Content", encoding='utf-8')

        _merge_body_sections(mock_ctx_with_citations)

        merged_file = drafts_dir / "02_main_body.md"
        assert merged_file.exists()


class TestWriteConclusion:
    """Tests for _write_conclusion helper."""

    def test_sets_conclusion_output(self, mock_ctx_with_citations):
        """Test that conclusion output is set."""
        mock_ctx_with_citations.body_output = "Body content"

        with patch('phases.compose.run_agent', return_value="# Conclusion"):
            _write_conclusion(mock_ctx_with_citations)

        assert mock_ctx_with_citations.conclusion_output != ""


class TestWriteAppendices:
    """Tests for _write_appendices helper."""

    def test_sets_appendix_output(self, mock_ctx_with_citations):
        """Test that appendix output is set for non-research papers."""
        mock_ctx_with_citations.intro_output = "Intro"
        mock_ctx_with_citations.body_output = "Body"
        mock_ctx_with_citations.conclusion_output = "Conclusion"

        with patch('phases.compose.run_agent', return_value="## Appendix A"):
            _write_appendices(mock_ctx_with_citations)

        assert mock_ctx_with_citations.appendix_output != ""

    def test_skips_for_research_paper(self, mock_ctx_with_citations):
        """Test that appendices are skipped for research papers."""
        mock_ctx_with_citations.word_targets['appendices'] = '0'
        mock_ctx_with_citations.intro_output = "Intro"
        mock_ctx_with_citations.body_output = "Body"
        mock_ctx_with_citations.conclusion_output = "Conclusion"

        with patch('phases.compose.run_agent') as mock_agent:
            _write_appendices(mock_ctx_with_citations)

        # run_agent should not be called when appendices target is '0'
        mock_agent.assert_not_called()
        assert mock_ctx_with_citations.appendix_output == ""


class TestRunComposePhase:
    """Tests for run_compose_phase orchestration."""

    def test_calls_all_writers(self, mock_ctx_with_citations):
        """Test that all section writers are called."""
        agent_calls = []

        def track_calls(model, name, **kwargs):
            agent_calls.append(name)
            if kwargs.get('save_to'):
                Path(kwargs['save_to']).parent.mkdir(parents=True, exist_ok=True)
                Path(kwargs['save_to']).write_text(f"Content for {name}", encoding='utf-8')
            return f"Output for {name}"

        with patch('phases.compose.run_agent', side_effect=track_calls):
            with patch('phases.compose.rate_limit_delay'):
                run_compose_phase(mock_ctx_with_citations)

        # Should have called Introduction, Lit Review, Methodology, Results, Discussion, Conclusion, Appendices
        assert len(agent_calls) >= 6  # At least 6 section agents

    def test_sets_all_outputs(self, mock_ctx_with_citations):
        """Test that all output fields are set after compose phase."""
        def mock_agent(model, name, save_to=None, **kwargs):
            content = f"Content for {name}"
            if save_to:
                Path(save_to).parent.mkdir(parents=True, exist_ok=True)
                Path(save_to).write_text(content, encoding='utf-8')
            return content

        with patch('phases.compose.run_agent', side_effect=mock_agent):
            with patch('phases.compose.rate_limit_delay'):
                run_compose_phase(mock_ctx_with_citations)

        assert mock_ctx_with_citations.intro_output != ""
        assert mock_ctx_with_citations.lit_review_output != ""
        assert mock_ctx_with_citations.methodology_output != ""
        assert mock_ctx_with_citations.results_output != ""
        assert mock_ctx_with_citations.discussion_output != ""
        assert mock_ctx_with_citations.body_output != ""
        assert mock_ctx_with_citations.conclusion_output != ""

    def test_includes_citation_summary(self, mock_ctx_with_citations):
        """Test that citation summary is included in prompts."""
        mock_ctx_with_citations.citation_summary = "UNIQUE_CITATION_SUMMARY_ZZZ"
        captured_inputs = []

        def capture_input(model, name, user_input, save_to=None, **kwargs):
            captured_inputs.append(user_input)
            if save_to:
                Path(save_to).parent.mkdir(parents=True, exist_ok=True)
                Path(save_to).write_text("Content", encoding='utf-8')
            return "Output"

        with patch('phases.compose.run_agent', side_effect=capture_input):
            with patch('phases.compose.rate_limit_delay'):
                run_compose_phase(mock_ctx_with_citations)

        # At least some prompts should include citation summary
        has_citation_summary = any("UNIQUE_CITATION_SUMMARY_ZZZ" in inp for inp in captured_inputs)
        assert has_citation_summary
