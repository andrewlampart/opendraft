#!/usr/bin/env python3
"""
ABOUTME: Pytest fixtures for OpenDraft engine tests
ABOUTME: Provides mock_ctx, mock_model, sample_citations for all test modules
"""

import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
from typing import Any, Dict, List
import tempfile

import pytest

# Add engine to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from phases.context import DraftContext
from utils.citation_database import Citation, CitationDatabase


@pytest.fixture
def temp_output_dir(tmp_path: Path) -> Dict[str, Path]:
    """Create temporary output directories matching the expected folder structure."""
    folders = {
        'root': tmp_path,
        'research': tmp_path / 'research',
        'papers': tmp_path / 'research' / 'papers',
        'drafts': tmp_path / 'drafts',
        'tools': tmp_path / 'tools',
        'exports': tmp_path / 'exports',
    }
    for folder in folders.values():
        folder.mkdir(parents=True, exist_ok=True)
    return folders


@pytest.fixture
def sample_citations() -> List[Citation]:
    """Create sample Citation objects for testing."""
    return [
        Citation(
            citation_id="cite_001",
            authors=["Smith, John", "Doe, Jane"],
            year=2023,
            title="Machine Learning in Healthcare: A Comprehensive Review",
            source_type="journal_article",
            journal="Nature Medicine",
            doi="10.1038/s41591-023-00001",
            abstract="This paper reviews the application of machine learning in healthcare settings.",
        ),
        Citation(
            citation_id="cite_002",
            authors=["Johnson, Alice"],
            year=2022,
            title="Deep Learning for Medical Image Analysis",
            source_type="journal_article",
            journal="IEEE Transactions on Medical Imaging",
            doi="10.1109/TMI.2022.00002",
            abstract="A study on deep learning techniques for analyzing medical images.",
        ),
        Citation(
            citation_id="cite_003",
            authors=["Williams, Bob", "Brown, Carol", "Davis, Eve"],
            year=2024,
            title="AI-Powered Diagnostics: Current State and Future Directions",
            source_type="conference_paper",
            journal="Proceedings of ICML 2024",
            abstract="Overview of AI diagnostic systems in clinical practice.",
        ),
    ]


@pytest.fixture
def sample_citation_database(sample_citations: List[Citation]) -> CitationDatabase:
    """Create a sample CitationDatabase for testing."""
    return CitationDatabase(
        citations=sample_citations,
        citation_style="APA 7th",
        draft_language="english",
    )


@pytest.fixture
def mock_config() -> MagicMock:
    """Create mock AppConfig for testing."""
    config = MagicMock()
    config.google_api_key = "test-api-key"
    config.model.model_name = "gemini-1.5-flash"
    config.model.temperature = 0.7
    config.paths.output_dir = Path("/tmp/opendraft_test")
    config.validation.enable_factcheck = False
    return config


@pytest.fixture
def mock_model() -> MagicMock:
    """
    Create mock GenerativeModel that returns canned responses.

    The model returns predictable text for different agent types based on
    keywords in the prompt.
    """
    model = MagicMock()

    def generate_response(prompt: str, *args, **kwargs) -> MagicMock:
        response = MagicMock()

        # Determine response based on prompt content
        if "Scout" in str(prompt) or "research" in str(prompt).lower():
            response.text = "## Research Summary\n\nFound 10 relevant papers on the topic."
        elif "Scribe" in str(prompt) or "summarize" in str(prompt).lower():
            response.text = "## Paper Summaries\n\n### Paper 1\nSummary of first paper.\n\n### Paper 2\nSummary of second paper."
        elif "Signal" in str(prompt) or "gaps" in str(prompt).lower():
            response.text = "## Research Gaps\n\n1. Gap in methodology\n2. Need for larger datasets"
        elif "Architect" in str(prompt) or "outline" in str(prompt).lower():
            response.text = "# Thesis Outline\n\n## 1. Introduction\n## 2. Literature Review\n## 3. Methodology"
        elif "Formatter" in str(prompt) or "format" in str(prompt).lower():
            response.text = "# Formatted Outline\n\n## Chapter 1: Introduction\n## Chapter 2: Main Body"
        elif "Introduction" in str(prompt):
            response.text = "# Introduction\n\nThis thesis explores the topic of machine learning in healthcare."
        elif "Literature" in str(prompt):
            response.text = "## 2.1 Literature Review\n\nPrevious research has shown..."
        elif "Methodology" in str(prompt):
            response.text = "## 2.2 Methodology\n\nThis study uses a mixed-methods approach."
        elif "Results" in str(prompt) or "Analysis" in str(prompt):
            response.text = "## 2.3 Results\n\nThe analysis revealed significant findings."
        elif "Discussion" in str(prompt):
            response.text = "## 2.4 Discussion\n\nThese findings have important implications."
        elif "Conclusion" in str(prompt):
            response.text = "# Conclusion\n\nIn summary, this research demonstrates..."
        elif "Appendices" in str(prompt) or "Appendix" in str(prompt):
            response.text = "## Appendix A: Additional Data\n\nSupplementary materials."
        elif "Thread" in str(prompt) or "Narrative" in str(prompt):
            response.text = "## Narrative Consistency Report\n\nNo major issues found."
        elif "Narrator" in str(prompt) or "Voice" in str(prompt):
            response.text = "## Voice Unification Report\n\nConsistent academic tone."
        elif "FactCheck" in str(prompt) or "claims" in str(prompt).lower():
            response.text = "[]"  # Empty JSON array for fact check extraction
        elif "abstract" in str(prompt).lower():
            response.text = "This thesis presents a comprehensive analysis..."
        else:
            response.text = "Generated content for: " + str(prompt)[:100]

        return response

    model.generate_content = MagicMock(side_effect=generate_response)
    return model


@pytest.fixture
def word_targets() -> Dict[str, Any]:
    """Return word count targets for master level."""
    return {
        'total': '25,000-30,000',
        'introduction': '2,500-3,000',
        'literature_review': '6,000-7,000',
        'methodology': '3,000-3,500',
        'results': '6,000-7,000',
        'discussion': '3,000-3,500',
        'conclusion': '1,500-2,000',
        'appendices': '2,000-3,000',
        'chapters': '7-10',
        'min_citations': 25,
        'deep_research_min_sources': 50,
        'estimated_time_minutes': '10-25',
    }


@pytest.fixture
def mock_ctx(
    temp_output_dir: Dict[str, Path],
    sample_citation_database: CitationDatabase,
    mock_config: MagicMock,
    mock_model: MagicMock,
    word_targets: Dict[str, Any],
) -> DraftContext:
    """
    Create a DraftContext with minimal valid data for testing.

    This context has all required fields populated and can be used
    to test individual phases in isolation.
    """
    ctx = DraftContext(
        topic="Machine Learning in Healthcare",
        language="en",
        academic_level="master",
        output_type="full",
        citation_style="apa",
        skip_validation=True,
        verbose=False,
        config=mock_config,
        model=mock_model,
        folders=temp_output_dir,
        word_targets=word_targets,
        language_name="English",
        language_instruction="\n\n**LANGUAGE REQUIREMENT:** Write in English.",
    )
    return ctx


@pytest.fixture
def mock_ctx_with_research(mock_ctx: DraftContext, sample_citations: List[Citation]) -> DraftContext:
    """
    Create a DraftContext with research phase outputs already populated.

    Useful for testing structure, citation, and compose phases.
    """
    mock_ctx.scout_result = {
        'count': len(sample_citations),
        'citations': sample_citations,
    }
    mock_ctx.scout_output = "## Scout Output\n\nFound 3 relevant papers."
    mock_ctx.scribe_output = "## Scribe Output\n\n### Paper 1\nSummary content."
    mock_ctx.signal_output = "## Research Gaps\n\n1. Gap in data quality\n2. Need for validation studies"
    return mock_ctx


@pytest.fixture
def mock_ctx_with_structure(mock_ctx_with_research: DraftContext) -> DraftContext:
    """
    Create a DraftContext with structure phase outputs already populated.

    Useful for testing citation and compose phases.
    """
    mock_ctx_with_research.architect_output = "# Thesis Outline\n\n## Introduction\n## Literature Review"
    mock_ctx_with_research.formatter_output = "# Formatted Outline\n\n## Chapter 1: Introduction\n## Chapter 2: Main Body\n## Chapter 3: Conclusion"
    return mock_ctx_with_research


@pytest.fixture
def mock_ctx_with_citations(
    mock_ctx_with_structure: DraftContext,
    sample_citation_database: CitationDatabase,
) -> DraftContext:
    """
    Create a DraftContext with citation management outputs already populated.

    Useful for testing compose and validate phases.
    """
    mock_ctx_with_structure.citation_database = sample_citation_database
    mock_ctx_with_structure.citation_summary = "## Citation Database\n\n3 citations available."
    return mock_ctx_with_structure


@pytest.fixture
def mock_ctx_fully_populated(mock_ctx_with_citations: DraftContext) -> DraftContext:
    """
    Create a DraftContext with all phase outputs populated.

    Useful for testing validate and compile phases.
    """
    ctx = mock_ctx_with_citations

    # Compose phase outputs
    ctx.intro_output = "# Introduction\n\nThis thesis explores machine learning in healthcare. {cite_001}"
    ctx.lit_review_output = "## 2.1 Literature Review\n\nPrevious research {cite_002} has shown..."
    ctx.methodology_output = "## 2.2 Methodology\n\nThis study uses a mixed-methods approach."
    ctx.results_output = "## 2.3 Results\n\nThe analysis revealed significant findings {cite_003}."
    ctx.discussion_output = "## 2.4 Discussion\n\nThese findings have important implications."
    ctx.body_output = f"{ctx.lit_review_output}\n\n{ctx.methodology_output}\n\n{ctx.results_output}\n\n{ctx.discussion_output}"
    ctx.conclusion_output = "# Conclusion\n\nIn summary, this research demonstrates the value of ML in healthcare."
    ctx.appendix_output = "## Appendix A: Data Tables\n\nSupplementary data."

    return ctx


@pytest.fixture
def mock_run_agent():
    """
    Fixture that patches run_agent to return canned responses.

    Usage:
        def test_something(mock_run_agent):
            with mock_run_agent as patched:
                # run_agent is now mocked
                result = some_function_that_uses_run_agent()
    """
    def _mock_run_agent(
        model,
        name: str,
        prompt_path: str,
        user_input: str,
        save_to=None,
        **kwargs,
    ) -> str:
        # Generate response based on agent name
        if "Scout" in name:
            output = "## Research Summary\n\nFound relevant papers."
        elif "Scribe" in name:
            output = "## Paper Summaries\n\nSummary content."
        elif "Signal" in name:
            output = "## Research Gaps\n\nIdentified gaps."
        elif "Architect" in name:
            output = "# Thesis Outline\n\n## Introduction"
        elif "Formatter" in name:
            output = "# Formatted Outline\n\n## Chapter 1"
        elif "Introduction" in name:
            output = "# Introduction\n\nIntro content."
        elif "Literature" in name:
            output = "## 2.1 Literature Review\n\nLit review content."
        elif "Methodology" in name:
            output = "## 2.2 Methodology\n\nMethodology content."
        elif "Results" in name or "Analysis" in name:
            output = "## 2.3 Results\n\nResults content."
        elif "Discussion" in name:
            output = "## 2.4 Discussion\n\nDiscussion content."
        elif "Conclusion" in name:
            output = "# Conclusion\n\nConclusion content."
        elif "Appendices" in name:
            output = "## Appendix A\n\nAppendix content."
        elif "Thread" in name:
            output = "## QA Report\n\nNo issues found."
        elif "Narrator" in name:
            output = "## Voice Report\n\nConsistent tone."
        elif "FactCheck" in name:
            output = "[]"
        else:
            output = f"Generated output for {name}"

        # Save to file if path provided
        if save_to:
            Path(save_to).parent.mkdir(parents=True, exist_ok=True)
            Path(save_to).write_text(output, encoding='utf-8')

        return output

    return patch('utils.agent_runner.run_agent', side_effect=_mock_run_agent)


@pytest.fixture
def mock_rate_limit_delay():
    """Mock rate_limit_delay to be a no-op for faster tests."""
    return patch('utils.agent_runner.rate_limit_delay', return_value=None)
