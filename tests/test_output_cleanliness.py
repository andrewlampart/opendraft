#!/usr/bin/env python3
"""
Tests for Tickets 017, 018, 019: Output Cleanliness — Defense-in-Depth

Validates that clean_agent_output() scrubs:
- Planning preambles (Ticket 017)
- Metadata leakage (Ticket 018)
- cite_MISSING markers (Ticket 019)

Run with: python -m pytest tests/test_output_cleanliness.py -v
"""

import sys
from pathlib import Path

import pytest

# Ensure engine package is importable
sys.path.insert(0, str(Path(__file__).parent.parent / "engine"))

from utils.text_utils import clean_agent_output


# ---------------------------------------------------------------------------
# Pass A — Planning preamble stripping (Ticket 017)
# ---------------------------------------------------------------------------

class TestStripPreamble:
    def test_strip_preamble_okay_i_understand(self):
        text = (
            "Okay, I understand the task. I need to write about housing policy.\n"
            "\n"
            "# 1. Introduction\n"
            "\n"
            "Housing policy has evolved significantly over the past decade.\n"
        )
        result = clean_agent_output(text)
        assert result.startswith("# 1. Introduction")
        assert "Okay, I understand" not in result

    def test_strip_preamble_heres_my_plan(self):
        text = (
            "Here's my plan for this section:\n"
            "1. First I'll cover the background\n"
            "2. Then discuss methodology\n"
            "\n"
            "## Literature Review\n"
            "\n"
            "The existing body of research demonstrates...\n"
        )
        result = clean_agent_output(text)
        assert result.startswith("## Literature Review")
        assert "Here's my plan" not in result

    def test_strip_preamble_i_will_write(self):
        text = (
            "I will write a comprehensive section covering the key themes.\n"
            "\n"
            "# Methodology\n"
            "\n"
            "This study employs a mixed-methods approach.\n"
        )
        result = clean_agent_output(text)
        assert result.startswith("# Methodology")
        assert "I will write" not in result

    def test_strip_preamble_let_me_first(self):
        text = (
            "Let me first outline the structure before diving in.\n"
            "\n"
            "## 2.1 Theoretical Framework\n"
            "\n"
            "The theoretical underpinnings of this research...\n"
        )
        result = clean_agent_output(text)
        assert result.startswith("## 2.1 Theoretical Framework")
        assert "Let me first" not in result

    def test_strip_preamble_numbered_planning(self):
        text = (
            "1. First I'll introduce the concept\n"
            "2. Then discuss the evidence\n"
            "3. Finally draw conclusions\n"
            "\n"
            "# Results\n"
            "\n"
            "The analysis revealed three key findings.\n"
        )
        result = clean_agent_output(text)
        assert result.startswith("# Results")

    def test_strip_preamble_preserves_content(self):
        text = (
            "# Introduction\n"
            "\n"
            "Housing policy has evolved significantly. "
            "This chapter examines the key developments.\n"
            "\n"
            "## 1.1 Background\n"
            "\n"
            "The origins of modern housing policy date back to...\n"
        )
        result = clean_agent_output(text)
        assert "# Introduction" in result
        assert "## 1.1 Background" in result
        assert "Housing policy has evolved" in result

    def test_strip_preamble_no_heading(self):
        """Content without any markdown heading should be preserved as-is."""
        text = (
            "The analysis of housing markets reveals several trends. "
            "First, affordability has declined in major urban centers. "
            "Second, government intervention has increased."
        )
        result = clean_agent_output(text)
        assert "The analysis of housing markets" in result


# ---------------------------------------------------------------------------
# Pass B — Metadata stripping (Ticket 018)
# ---------------------------------------------------------------------------

class TestStripMetadata:
    def test_strip_metadata_section_line(self):
        text = (
            "**Section:** Literature Review\n"
            "\n"
            "The literature on this topic is extensive.\n"
        )
        result = clean_agent_output(text)
        assert "**Section:**" not in result
        assert "The literature on this topic is extensive." in result

    def test_strip_metadata_word_count(self):
        text = (
            "The findings suggest a strong correlation.\n"
            "\n"
            "**Word Count:** 2,294 words\n"
        )
        result = clean_agent_output(text)
        assert "**Word Count:**" not in result
        assert "The findings suggest a strong correlation." in result

    def test_strip_metadata_status(self):
        text = (
            "**Status:** Draft v1\n"
            "\n"
            "# Introduction\n"
            "\n"
            "This chapter introduces the core argument.\n"
        )
        result = clean_agent_output(text)
        assert "**Status:**" not in result
        assert "This chapter introduces the core argument." in result

    def test_strip_metadata_citations_used_section(self):
        text = (
            "# Discussion\n"
            "\n"
            "The results confirm the hypothesis.\n"
            "\n"
            "## Citations Used\n"
            "\n"
            "- Smith (2020)\n"
            "- Jones (2019)\n"
            "- Brown et al. (2021)\n"
        )
        result = clean_agent_output(text)
        assert "## Citations Used" not in result
        assert "Smith (2020)" not in result
        assert "The results confirm the hypothesis." in result

    def test_strip_metadata_notes_for_revision(self):
        text = (
            "# Conclusion\n"
            "\n"
            "In summary, the evidence supports our thesis.\n"
            "\n"
            "## Notes for Revision\n"
            "\n"
            "- Need to strengthen argument in paragraph 3\n"
            "- Consider adding more recent sources\n"
        )
        result = clean_agent_output(text)
        assert "## Notes for Revision" not in result
        assert "Need to strengthen" not in result
        assert "In summary, the evidence supports our thesis." in result

    def test_strip_metadata_word_count_breakdown(self):
        text = (
            "# Results\n"
            "\n"
            "Three key themes emerged from the data.\n"
            "\n"
            "## Word Count Breakdown\n"
            "\n"
            "- Introduction: 450 words\n"
            "- Body: 1,800 words\n"
            "- Conclusion: 350 words\n"
        )
        result = clean_agent_output(text)
        assert "## Word Count Breakdown" not in result
        assert "Introduction: 450 words" not in result
        assert "Three key themes emerged from the data." in result

    def test_strip_metadata_preserves_content(self):
        text = (
            "# 3. Methodology\n"
            "\n"
            "This study employs a mixed-methods approach combining "
            "quantitative survey data (n=500) with qualitative interviews "
            "(n=25). The research design follows the framework proposed "
            "by Creswell (2014), adapted for the housing policy context.\n"
        )
        result = clean_agent_output(text)
        assert "mixed-methods approach" in result
        assert "Creswell (2014)" in result


# ---------------------------------------------------------------------------
# Pass C — cite_MISSING stripping (Ticket 019)
# ---------------------------------------------------------------------------

class TestStripCiteMissing:
    def test_strip_cite_missing_basic(self):
        text = "Recent studies {cite_MISSING: housing affordability 2023} show a decline."
        result = clean_agent_output(text)
        assert "{cite_MISSING" not in result
        assert "Recent studies show a decline." in result

    def test_strip_cite_missing_no_space(self):
        text = "According to {cite_MISSING:urban planning theory}, cities evolve."
        result = clean_agent_output(text)
        assert "{cite_MISSING" not in result
        assert "According to, cities evolve." in result

    def test_strip_cite_missing_preserves_valid(self):
        text = "As shown by prior research {cite_001}, the trend is clear."
        result = clean_agent_output(text)
        assert "{cite_001}" in result

    def test_strip_cite_missing_multiple(self):
        text = (
            "Evidence {cite_MISSING: topic A} suggests that "
            "further investigation {cite_MISSING: topic B} is needed."
        )
        result = clean_agent_output(text)
        assert "{cite_MISSING" not in result
        assert "Evidence suggests that further investigation is needed." in result


# ---------------------------------------------------------------------------
# Combined pass
# ---------------------------------------------------------------------------

class TestCleanAgentOutputCombined:
    def test_clean_agent_output_combined(self):
        """All three passes should work together in sequence."""
        text = (
            "Okay, I understand. I'll write the methodology section now.\n"
            "\n"
            "**Section:** Methodology\n"
            "**Word Count:** 1,500 words\n"
            "**Status:** Draft v1\n"
            "\n"
            "# 3. Methodology\n"
            "\n"
            "This study employs a mixed-methods approach {cite_MISSING: methods reference}. "
            "The framework follows established protocols {cite_042}.\n"
            "\n"
            "## Notes for Revision\n"
            "\n"
            "- Add more detail on sampling strategy\n"
        )
        result = clean_agent_output(text)
        # Pass A: preamble removed
        assert "Okay, I understand" not in result
        # Pass B: metadata removed
        assert "**Section:**" not in result
        assert "**Word Count:**" not in result
        assert "**Status:**" not in result
        assert "## Notes for Revision" not in result
        assert "sampling strategy" not in result
        # Pass C: cite_MISSING removed
        assert "{cite_MISSING" not in result
        # Content preserved
        assert "# 3. Methodology" in result
        assert "mixed-methods approach" in result
        assert "{cite_042}" in result

    def test_clean_agent_output_empty_string(self):
        assert clean_agent_output("") == ""

    def test_clean_agent_output_none_passthrough(self):
        """None-ish inputs shouldn't crash."""
        assert clean_agent_output("") == ""
        assert clean_agent_output("   ") == "   "
