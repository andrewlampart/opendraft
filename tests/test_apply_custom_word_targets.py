"""Tests for apply_custom_word_targets (wizard page/publication scope)."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "engine"))

from draft_generator import apply_custom_word_targets, get_word_count_targets


def test_publication_count_only():
    base = get_word_count_targets("master")
    out = apply_custom_word_targets(base, publication_count=40)
    assert out["min_citations"] == 40
    assert out["deep_research_min_sources"] == 40
    assert out["total"] == base["total"]


def test_pages_scale_word_targets():
    base = get_word_count_targets("master")
    out = apply_custom_word_targets(
        base, pages_min=40, pages_max=40, publication_count=None
    )
    assert out["min_citations"] == base["min_citations"]
    lo, hi = out["total"].replace(",", "").split("-")
    assert int(lo) < int(base["total"].split("-")[0].replace(",", ""))


def test_pages_and_publications_combined():
    base = get_word_count_targets("bachelor")
    out = apply_custom_word_targets(
        base, pages_min=80, pages_max=100, publication_count=20
    )
    assert out["min_citations"] == 20
    assert out["deep_research_min_sources"] == 20
    assert "introduction" in out
    assert out["appendices"] != "0" or base["appendices"] == "0"


def test_appendices_zero_preserved():
    base = get_word_count_targets("research_paper")
    out = apply_custom_word_targets(base, pages_min=12, pages_max=15)
    assert out["appendices"] == "0"


def test_publication_clamp():
    base = get_word_count_targets("master")
    out = apply_custom_word_targets(base, publication_count=500)
    assert out["min_citations"] == 200
    out2 = apply_custom_word_targets(base, publication_count=1)
    assert out2["min_citations"] == 5
