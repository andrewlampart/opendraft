#!/usr/bin/env python3
"""
ABOUTME: Unit tests for DraftContext dataclass and validation helpers
ABOUTME: Tests PhaseValidationError and validate_phase_output function
"""

import pytest
from pathlib import Path

from phases.context import DraftContext, PhaseValidationError, validate_phase_output


class TestDraftContext:
    """Tests for DraftContext dataclass creation and mutation."""

    def test_create_minimal_context(self):
        """Test creating context with minimal required fields."""
        ctx = DraftContext(topic="Test Topic")
        assert ctx.topic == "Test Topic"
        assert ctx.language == "en"
        assert ctx.academic_level == "master"
        assert ctx.output_type == "full"

    def test_create_context_with_all_fields(self, temp_output_dir, mock_config, mock_model, word_targets):
        """Test creating context with all optional fields."""
        ctx = DraftContext(
            topic="Machine Learning in Healthcare",
            language="de",
            academic_level="phd",
            output_type="expose",
            citation_style="ieee",
            skip_validation=False,
            verbose=True,
            blurb="Focus on neural networks",
            author_name="John Doe",
            institution="MIT",
            department="CS",
            faculty="Engineering",
            advisor="Dr. Smith",
            second_examiner="Dr. Jones",
            location="Boston",
            student_id="12345",
            config=mock_config,
            model=mock_model,
            folders=temp_output_dir,
            word_targets=word_targets,
            language_name="German",
            language_instruction="Write in German",
        )
        assert ctx.topic == "Machine Learning in Healthcare"
        assert ctx.language == "de"
        assert ctx.academic_level == "phd"
        assert ctx.author_name == "John Doe"

    def test_context_default_output_fields_are_empty(self):
        """Test that output fields start empty."""
        ctx = DraftContext(topic="Test")
        assert ctx.scout_result is None
        assert ctx.scout_output == ""
        assert ctx.scribe_output == ""
        assert ctx.intro_output == ""
        assert ctx.conclusion_output == ""
        assert ctx.citation_database is None

    def test_context_mutation(self, mock_ctx):
        """Test that context fields can be mutated."""
        mock_ctx.scout_output = "New scout output"
        mock_ctx.intro_output = "New intro"
        assert mock_ctx.scout_output == "New scout output"
        assert mock_ctx.intro_output == "New intro"


class TestPhaseValidationError:
    """Tests for PhaseValidationError exception class."""

    def test_create_error_with_message(self):
        """Test creating error with phase and message."""
        error = PhaseValidationError(phase="research", message="Scout failed")
        assert error.phase == "research"
        assert "research" in str(error)
        assert "Scout failed" in str(error)
        assert error.missing_fields == []

    def test_create_error_with_missing_fields(self):
        """Test creating error with missing fields list."""
        error = PhaseValidationError(
            phase="compose",
            message="Missing outputs",
            missing_fields=["intro_output", "body_output"],
        )
        assert error.missing_fields == ["intro_output", "body_output"]
        assert "compose" in str(error)

    def test_error_is_exception(self):
        """Test that PhaseValidationError is an Exception."""
        error = PhaseValidationError(phase="test", message="test error")
        assert isinstance(error, Exception)
        with pytest.raises(PhaseValidationError):
            raise error


class TestValidatePhaseOutput:
    """Tests for validate_phase_output helper function."""

    def test_validate_passes_with_valid_fields(self, mock_ctx):
        """Test validation passes when all required fields are present."""
        mock_ctx.scout_output = "Valid scout output with content"
        mock_ctx.scribe_output = "Valid scribe output with content"

        # Should not raise
        validate_phase_output(
            mock_ctx,
            phase_name="research",
            required_fields=["scout_output", "scribe_output"],
        )

    def test_validate_fails_on_missing_field(self, mock_ctx):
        """Test validation fails when required field is None."""
        mock_ctx.scout_result = None

        with pytest.raises(PhaseValidationError) as exc_info:
            validate_phase_output(
                mock_ctx,
                phase_name="research",
                required_fields=["scout_result"],
            )

        assert exc_info.value.phase == "research"
        assert "scout_result" in exc_info.value.missing_fields

    def test_validate_fails_on_empty_string(self, mock_ctx):
        """Test validation fails when string field is empty."""
        mock_ctx.scout_output = ""
        mock_ctx.scribe_output = "   "  # whitespace only

        with pytest.raises(PhaseValidationError) as exc_info:
            validate_phase_output(
                mock_ctx,
                phase_name="research",
                required_fields=["scout_output", "scribe_output"],
            )

        assert "scout_output" in exc_info.value.missing_fields
        assert "scribe_output" in exc_info.value.missing_fields

    def test_validate_fails_on_empty_list(self, mock_ctx):
        """Test validation fails when list field is empty."""
        mock_ctx.scout_result = {'citations': []}

        # This should pass as scout_result is not empty (it's a dict)
        validate_phase_output(
            mock_ctx,
            phase_name="research",
            required_fields=["scout_result"],
        )

    def test_validate_min_chars_passes(self, mock_ctx):
        """Test min_chars validation passes with sufficient content."""
        mock_ctx.intro_output = "A" * 500

        validate_phase_output(
            mock_ctx,
            phase_name="compose",
            required_fields=["intro_output"],
            min_chars={"intro_output": 200},
        )

    def test_validate_min_chars_fails(self, mock_ctx):
        """Test min_chars validation fails with insufficient content."""
        mock_ctx.intro_output = "Short"

        with pytest.raises(PhaseValidationError) as exc_info:
            validate_phase_output(
                mock_ctx,
                phase_name="compose",
                required_fields=["intro_output"],
                min_chars={"intro_output": 200},
            )

        assert "below minimum size" in str(exc_info.value)

    def test_validate_multiple_fields(self, mock_ctx):
        """Test validation of multiple fields at once."""
        mock_ctx.intro_output = "Introduction content"
        mock_ctx.body_output = "Body content"
        mock_ctx.conclusion_output = ""  # Missing

        with pytest.raises(PhaseValidationError) as exc_info:
            validate_phase_output(
                mock_ctx,
                phase_name="compose",
                required_fields=["intro_output", "body_output", "conclusion_output"],
            )

        assert "conclusion_output" in exc_info.value.missing_fields
        assert "intro_output" not in exc_info.value.missing_fields
