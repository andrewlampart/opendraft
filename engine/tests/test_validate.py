#!/usr/bin/env python3
"""
ABOUTME: Unit tests for validation phase
ABOUTME: Tests Thread, Narrator, and FactCheck QA agents
"""

import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

from phases.validate import (
    run_validate_phase,
    _build_qa_content,
    _run_thread,
    _run_narrator,
    _run_factcheck,
)


class TestBuildQAContent:
    """Tests for _build_qa_content helper."""

    def test_includes_all_sections(self, mock_ctx_fully_populated):
        """Test that QA content includes all chapter sections."""
        qa_content = _build_qa_content(mock_ctx_fully_populated)

        assert "Introduction" in qa_content
        assert "Literature Review" in qa_content
        assert "Methodology" in qa_content
        assert "Results" in qa_content
        assert "Discussion" in qa_content
        assert "Conclusion" in qa_content

    def test_includes_topic(self, mock_ctx_fully_populated):
        """Test that topic is included in QA content."""
        qa_content = _build_qa_content(mock_ctx_fully_populated)

        assert mock_ctx_fully_populated.topic in qa_content

    def test_truncates_long_sections(self, mock_ctx_fully_populated):
        """Test that long sections are truncated."""
        mock_ctx_fully_populated.intro_output = "A" * 5000

        qa_content = _build_qa_content(mock_ctx_fully_populated)

        # Should be truncated to ~1500 chars for intro
        intro_section = qa_content.split("Chapter 1: Introduction")[1].split("Chapter 2")[0]
        assert len(intro_section) < 3000

    def test_reads_from_files_when_available(self, mock_ctx_fully_populated):
        """Test that content is read from draft files when they exist."""
        drafts_dir = mock_ctx_fully_populated.folders['drafts']
        (drafts_dir / "02_1_literature_review.md").write_text("FILE_LIT_REVIEW_CONTENT", encoding='utf-8')

        qa_content = _build_qa_content(mock_ctx_fully_populated)

        assert "FILE_LIT_REVIEW_CONTENT" in qa_content


class TestRunThread:
    """Tests for _run_thread helper."""

    def test_calls_thread_agent(self, mock_ctx_fully_populated):
        """Test that Thread agent is called."""
        with patch('phases.validate.run_agent') as mock_agent:
            mock_agent.return_value = "## QA Report"

            _run_thread(mock_ctx_fully_populated, "QA Content")

            mock_agent.assert_called_once()
            call_kwargs = mock_agent.call_args[1]
            assert "Thread" in call_kwargs['name']

    def test_saves_qa_report(self, mock_ctx_fully_populated):
        """Test that QA report is saved to correct location."""
        saved_path = None

        def capture_save(model, name, save_to, **kwargs):
            nonlocal saved_path
            saved_path = save_to
            return "## Report"

        with patch('phases.validate.run_agent', side_effect=capture_save):
            _run_thread(mock_ctx_fully_populated, "Content")

        assert saved_path is not None
        assert "qa_narrative_consistency" in str(saved_path)

    def test_continues_on_failure(self, mock_ctx_fully_populated):
        """Test that Thread failure doesn't raise exception."""
        with patch('phases.validate.run_agent', side_effect=Exception("API Error")):
            # Should not raise
            _run_thread(mock_ctx_fully_populated, "Content")


class TestRunNarrator:
    """Tests for _run_narrator helper."""

    def test_calls_narrator_agent(self, mock_ctx_fully_populated):
        """Test that Narrator agent is called."""
        with patch('phases.validate.run_agent') as mock_agent:
            mock_agent.return_value = "## Voice Report"

            _run_narrator(mock_ctx_fully_populated, "QA Content")

            mock_agent.assert_called_once()
            call_kwargs = mock_agent.call_args[1]
            assert "Narrator" in call_kwargs['name']

    def test_includes_academic_level(self, mock_ctx_fully_populated):
        """Test that academic level is included in prompt."""
        captured_input = None

        def capture_input(model, name, user_input, **kwargs):
            nonlocal captured_input
            captured_input = user_input
            return "## Report"

        mock_ctx_fully_populated.academic_level = "phd"

        with patch('phases.validate.run_agent', side_effect=capture_input):
            _run_narrator(mock_ctx_fully_populated, "Content")

        assert "phd" in captured_input.lower()

    def test_continues_on_failure(self, mock_ctx_fully_populated):
        """Test that Narrator failure doesn't raise exception."""
        with patch('phases.validate.run_agent', side_effect=Exception("API Error")):
            # Should not raise
            _run_narrator(mock_ctx_fully_populated, "Content")


class TestRunFactcheck:
    """Tests for _run_factcheck helper."""

    def test_skips_when_disabled(self, mock_ctx_fully_populated):
        """Test that factcheck is skipped when disabled in config."""
        mock_ctx_fully_populated.config.validation.enable_factcheck = False

        with patch('phases.validate.run_agent') as mock_agent:
            _run_factcheck(mock_ctx_fully_populated, "Content")

            mock_agent.assert_not_called()

    def test_extracts_claims(self, mock_ctx_fully_populated):
        """Test that factcheck extracts claims when enabled."""
        mock_ctx_fully_populated.config.validation.enable_factcheck = True

        with patch('phases.validate.run_agent', return_value="[]"):
            _run_factcheck(mock_ctx_fully_populated, "Content")

    def test_handles_invalid_json(self, mock_ctx_fully_populated):
        """Test that invalid JSON from claim extraction is handled."""
        mock_ctx_fully_populated.config.validation.enable_factcheck = True

        with patch('phases.validate.run_agent', return_value="not valid json"):
            # Should not raise
            _run_factcheck(mock_ctx_fully_populated, "Content")


class TestRunValidatePhase:
    """Tests for run_validate_phase orchestration."""

    def test_calls_all_qa_agents(self, mock_ctx_fully_populated):
        """Test that all QA agents are called."""
        agent_calls = []

        def track_calls(model, name, **kwargs):
            agent_calls.append(name)
            return "## Report"

        with patch('phases.validate.run_agent', side_effect=track_calls):
            with patch('phases.validate.rate_limit_delay'):
                run_validate_phase(mock_ctx_fully_populated)

        # Should call Thread and Narrator (FactCheck disabled by default)
        assert any("Thread" in call for call in agent_calls)
        assert any("Narrator" in call for call in agent_calls)

    def test_no_context_mutations(self, mock_ctx_fully_populated):
        """Test that validate phase doesn't mutate compose outputs."""
        original_intro = mock_ctx_fully_populated.intro_output
        original_body = mock_ctx_fully_populated.body_output
        original_conclusion = mock_ctx_fully_populated.conclusion_output

        with patch('phases.validate.run_agent', return_value="## Report"):
            with patch('phases.validate.rate_limit_delay'):
                run_validate_phase(mock_ctx_fully_populated)

        assert mock_ctx_fully_populated.intro_output == original_intro
        assert mock_ctx_fully_populated.body_output == original_body
        assert mock_ctx_fully_populated.conclusion_output == original_conclusion

    def test_writes_qa_files(self, mock_ctx_fully_populated):
        """Test that QA report files are created."""
        def save_file(model, name, save_to, **kwargs):
            if save_to:
                Path(save_to).parent.mkdir(parents=True, exist_ok=True)
                Path(save_to).write_text("## Report", encoding='utf-8')
            return "## Report"

        with patch('phases.validate.run_agent', side_effect=save_file):
            with patch('phases.validate.rate_limit_delay'):
                run_validate_phase(mock_ctx_fully_populated)

        drafts_dir = mock_ctx_fully_populated.folders['drafts']
        assert (drafts_dir / "qa_narrative_consistency.md").exists()
        assert (drafts_dir / "qa_voice_unification.md").exists()
