#!/usr/bin/env python3
"""
ABOUTME: Unit tests for structure phase
ABOUTME: Tests Architect and Formatter agents
"""

import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

from phases.structure import run_structure_phase


class TestRunStructurePhase:
    """Tests for run_structure_phase function."""

    def test_structure_phase_sets_outputs(self, mock_ctx_with_research):
        """Test that structure phase sets architect and formatter outputs."""
        with patch('phases.structure.run_agent') as mock_run_agent:
            mock_run_agent.side_effect = [
                "# Thesis Outline\n\n## Introduction\n## Literature Review",
                "# Formatted Outline\n\n## Chapter 1: Introduction",
            ]

            with patch('phases.structure.rate_limit_delay'):
                run_structure_phase(mock_ctx_with_research)

        assert mock_ctx_with_research.architect_output != ""
        assert "Outline" in mock_ctx_with_research.architect_output
        assert mock_ctx_with_research.formatter_output != ""

    def test_structure_phase_calls_both_agents(self, mock_ctx_with_research):
        """Test that both Architect and Formatter agents are called."""
        agent_calls = []

        def track_calls(model, name, **kwargs):
            agent_calls.append(name)
            return f"Output from {name}"

        with patch('phases.structure.run_agent', side_effect=track_calls):
            with patch('phases.structure.rate_limit_delay'):
                run_structure_phase(mock_ctx_with_research)

        assert len(agent_calls) == 2
        assert any("Architect" in call for call in agent_calls)
        assert any("Formatter" in call for call in agent_calls)

    def test_structure_phase_uses_signal_output(self, mock_ctx_with_research):
        """Test that structure phase uses signal output from research."""
        captured_input = None

        def capture_input(model, name, user_input, **kwargs):
            nonlocal captured_input
            if "Architect" in name:
                captured_input = user_input
            return "Output"

        with patch('phases.structure.run_agent', side_effect=capture_input):
            with patch('phases.structure.rate_limit_delay'):
                run_structure_phase(mock_ctx_with_research)

        assert captured_input is not None
        # Signal output should be included in architect prompt
        assert mock_ctx_with_research.signal_output[:50] in captured_input or "gaps" in captured_input.lower()

    def test_structure_phase_saves_files(self, mock_ctx_with_research):
        """Test that structure phase saves outline files."""
        with patch('phases.structure.run_agent') as mock_agent:
            mock_agent.side_effect = [
                "# Outline Content",
                "# Formatted Content",
            ]

            with patch('phases.structure.rate_limit_delay'):
                run_structure_phase(mock_ctx_with_research)

        # Check save_to parameters were passed
        calls = mock_agent.call_args_list
        assert len(calls) == 2

        # First call should save to 00_outline.md
        first_call_kwargs = calls[0][1]
        assert "00_outline" in str(first_call_kwargs.get('save_to', ''))

        # Second call should save to 00_formatted_outline.md
        second_call_kwargs = calls[1][1]
        assert "formatted_outline" in str(second_call_kwargs.get('save_to', ''))

    def test_structure_phase_includes_academic_level(self, mock_ctx_with_research):
        """Test that academic level is included in architect prompt."""
        captured_inputs = []

        def capture_input(model, name, user_input, **kwargs):
            captured_inputs.append((name, user_input))
            return "Output"

        mock_ctx_with_research.academic_level = "phd"

        with patch('phases.structure.run_agent', side_effect=capture_input):
            with patch('phases.structure.rate_limit_delay'):
                run_structure_phase(mock_ctx_with_research)

        architect_input = next(inp for name, inp in captured_inputs if "Architect" in name)
        assert "phd" in architect_input.lower() or "dissertation" in architect_input.lower()

    def test_structure_phase_updates_tracker(self, mock_ctx_with_research):
        """Test that progress tracker is updated during structure phase."""
        mock_tracker = MagicMock()
        mock_ctx_with_research.tracker = mock_tracker

        with patch('phases.structure.run_agent', return_value="Output"):
            with patch('phases.structure.rate_limit_delay'):
                run_structure_phase(mock_ctx_with_research)

        # Tracker should have been updated
        assert mock_tracker.log_activity.called or mock_tracker.update_phase.called
