#!/usr/bin/env python3
"""
ABOUTME: DraftContext dataclass — mutable shared state for inter-phase communication
ABOUTME: Each phase reads inputs from ctx and writes outputs back to ctx
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


class PhaseValidationError(Exception):
    """
    Raised when inter-phase validation fails.

    Contains phase name and specific validation failures to enable
    fail-fast behavior and clear error messages.
    """

    def __init__(self, phase: str, message: str, missing_fields: Optional[List[str]] = None):
        self.phase = phase
        self.missing_fields = missing_fields or []
        super().__init__(f"[{phase}] {message}")


def validate_phase_output(
    ctx: "DraftContext",
    phase_name: str,
    required_fields: List[str],
    min_chars: Optional[Dict[str, int]] = None,
) -> None:
    """
    Validate that a phase has produced required outputs before proceeding.

    Args:
        ctx: The DraftContext to validate
        phase_name: Name of the phase being validated (for error messages)
        required_fields: List of ctx attribute names that must be non-empty
        min_chars: Optional dict mapping field names to minimum character counts

    Raises:
        PhaseValidationError: If any required field is missing or too short
    """
    min_chars = min_chars or {}
    missing = []
    too_short = []

    for field_name in required_fields:
        value = getattr(ctx, field_name, None)

        # Check if field exists and is non-empty
        if value is None:
            missing.append(field_name)
        elif isinstance(value, str) and not value.strip():
            missing.append(field_name)
        elif isinstance(value, (list, dict)) and len(value) == 0:
            missing.append(field_name)

        # Check minimum character count for string fields
        if field_name in min_chars and isinstance(value, str):
            if len(value) < min_chars[field_name]:
                too_short.append(f"{field_name} ({len(value)}/{min_chars[field_name]} chars)")

    if missing:
        raise PhaseValidationError(
            phase=phase_name,
            message=f"Missing required outputs: {', '.join(missing)}",
            missing_fields=missing,
        )

    if too_short:
        raise PhaseValidationError(
            phase=phase_name,
            message=f"Outputs below minimum size: {', '.join(too_short)}",
            missing_fields=[],
        )


@dataclass
class DraftContext:
    """
    Mutable inter-phase communication bus for draft generation.

    Each phase function takes a DraftContext, reads its inputs,
    and writes its outputs back onto the same object.
    """

    # ------------------------------------------------------------------
    # User inputs (set once at initialization)
    # ------------------------------------------------------------------
    topic: str = ""
    language: str = "en"
    academic_level: str = "master"
    output_type: str = "full"  # 'full' or 'expose'
    citation_style: str = "apa"  # 'apa', 'ieee', or 'nalt'
    skip_validation: bool = True
    verbose: bool = True
    blurb: Optional[str] = None

    # Academic metadata (optional, for cover page)
    author_name: Optional[str] = None
    institution: Optional[str] = None
    department: Optional[str] = None
    faculty: Optional[str] = None
    advisor: Optional[str] = None
    second_examiner: Optional[str] = None
    location: Optional[str] = None
    student_id: Optional[str] = None

    # ------------------------------------------------------------------
    # Infrastructure (set during initialization)
    # ------------------------------------------------------------------
    config: Any = None  # AppConfig instance
    model: Any = None  # GenerativeModel instance
    folders: Dict[str, Path] = field(default_factory=dict)
    word_targets: Dict[str, Any] = field(default_factory=dict)
    language_name: str = ""
    language_instruction: str = ""

    # Progress reporting (optional)
    tracker: Any = None  # ProgressTracker
    streamer: Any = None  # MilestoneStreamer

    # ------------------------------------------------------------------
    # Research phase outputs
    # ------------------------------------------------------------------
    scout_result: Optional[Dict[str, Any]] = None
    scout_output: str = ""
    scribe_output: str = ""
    signal_output: str = ""

    # ------------------------------------------------------------------
    # Structure phase outputs
    # ------------------------------------------------------------------
    architect_output: str = ""
    formatter_output: str = ""

    # ------------------------------------------------------------------
    # Citation management outputs
    # ------------------------------------------------------------------
    citation_database: Any = None  # CitationDatabase
    citation_summary: str = ""

    # ------------------------------------------------------------------
    # Compose phase outputs
    # ------------------------------------------------------------------
    intro_output: str = ""
    lit_review_output: str = ""
    methodology_output: str = ""
    results_output: str = ""
    discussion_output: str = ""
    body_output: str = ""
    conclusion_output: str = ""
    appendix_output: str = ""

    # ------------------------------------------------------------------
    # Token tracking (optional)
    # ------------------------------------------------------------------
    token_tracker: Any = None  # TokenTracker
