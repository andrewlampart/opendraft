#!/usr/bin/env python3
"""
ABOUTME: E2E test runner for OpenDraft pipeline
ABOUTME: Runs generate_draft() with diverse topics and tracks timing/errors

Usage:
    python test_pipeline.py                    # Run all 5 test topics
    python test_pipeline.py --topic 1          # Run only topic 1 (Technical)
    python test_pipeline.py --mock             # Run with mocked LLM (no API calls)
    python test_pipeline.py --verbose          # Show detailed output
"""

import sys
import time
import argparse
import traceback
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field

# Add engine to path
sys.path.insert(0, str(Path(__file__).parent))


@dataclass
class TestResult:
    """Result of a single test run."""
    topic_id: int
    topic: str
    language: str
    academic_level: str
    output_type: str
    success: bool
    duration_seconds: float
    pdf_path: Optional[Path] = None
    docx_path: Optional[Path] = None
    error: Optional[str] = None
    traceback: Optional[str] = None
    phase_timings: Dict[str, float] = field(default_factory=dict)


# Test configurations
TEST_TOPICS = [
    {
        'id': 1,
        'topic': "Machine Learning Applications in Healthcare Diagnostics",
        'language': "en",
        'academic_level': "master",
        'output_type': "full",
        'description': "Technical - ML/Healthcare",
    },
    {
        'id': 2,
        'topic': "The Impact of Social Media on Democratic Processes",
        'language': "en",
        'academic_level': "master",
        'output_type': "full",
        'description': "Humanities - Social Media",
    },
    {
        'id': 3,
        'topic': "Renewable Energy Adoption in Urban Areas",
        'language': "en",
        'academic_level': "master",
        'output_type': "expose",
        'description': "Short Expose Mode",
    },
    {
        'id': 4,
        'topic': "Künstliche Intelligenz in der Medizin",
        'language': "de",
        'academic_level': "master",
        'output_type': "full",
        'description': "Non-English (German)",
    },
    {
        'id': 5,
        'topic': "Quantum Computing for Cryptographic Security",
        'language': "en",
        'academic_level': "phd",
        'output_type': "full",
        'description': "PhD Level",
    },
]


def run_test(config: dict, output_base: Path, verbose: bool = True, mock: bool = False) -> TestResult:
    """
    Run a single test configuration.

    Args:
        config: Test configuration dict
        output_base: Base directory for outputs
        verbose: Show detailed progress
        mock: Use mocked LLM calls (no API)

    Returns:
        TestResult with success/failure info
    """
    topic_id = config['id']
    topic = config['topic']
    language = config['language']
    academic_level = config['academic_level']
    output_type = config['output_type']

    print(f"\n{'='*70}")
    print(f"TEST {topic_id}: {config['description']}")
    print(f"{'='*70}")
    print(f"Topic: {topic}")
    print(f"Language: {language}")
    print(f"Level: {academic_level}")
    print(f"Type: {output_type}")
    print(f"{'='*70}")

    output_dir = output_base / f"test_{topic_id}_{language}_{academic_level}"
    start_time = time.time()

    try:
        if mock:
            # Run with mocked LLM - for fast testing
            pdf_path, docx_path = _run_mocked(
                topic=topic,
                language=language,
                academic_level=academic_level,
                output_type=output_type,
                output_dir=output_dir,
                verbose=verbose,
            )
        else:
            # Run with real LLM - for e2e testing
            from draft_generator import generate_draft

            pdf_path, docx_path = generate_draft(
                topic=topic,
                language=language,
                academic_level=academic_level,
                output_dir=output_dir,
                output_type=output_type,
                skip_validation=True,
                verbose=verbose,
            )

        duration = time.time() - start_time

        print(f"\n✅ TEST {topic_id} PASSED in {duration:.1f}s")
        print(f"   PDF: {pdf_path}")
        print(f"   DOCX: {docx_path}")

        return TestResult(
            topic_id=topic_id,
            topic=topic,
            language=language,
            academic_level=academic_level,
            output_type=output_type,
            success=True,
            duration_seconds=duration,
            pdf_path=pdf_path,
            docx_path=docx_path,
        )

    except Exception as e:
        duration = time.time() - start_time
        error_msg = str(e)
        tb = traceback.format_exc()

        print(f"\n❌ TEST {topic_id} FAILED after {duration:.1f}s")
        print(f"   Error: {error_msg}")
        if verbose:
            print(f"\n   Traceback:\n{tb}")

        return TestResult(
            topic_id=topic_id,
            topic=topic,
            language=language,
            academic_level=academic_level,
            output_type=output_type,
            success=False,
            duration_seconds=duration,
            error=error_msg,
            traceback=tb,
        )


def _run_mocked(
    topic: str,
    language: str,
    academic_level: str,
    output_type: str,
    output_dir: Path,
    verbose: bool = True,
) -> Tuple[Path, Path]:
    """
    Run pipeline with mocked LLM calls for fast testing.

    Returns (pdf_path, docx_path)
    """
    from contextlib import ExitStack
    from unittest.mock import patch, MagicMock
    from utils.citation_database import Citation, CitationDatabase

    # Create mock citations
    mock_citations = [
        Citation(
            citation_id=f"cite_{i:03d}",
            authors=[f"Author{i}, Test"],
            year=2023 - i,
            title=f"Mock Paper {i}: {topic[:30]}",
            source_type="journal_article",
            journal="Mock Journal",
            doi=f"10.1000/mock{i}",
            abstract=f"Abstract for mock paper {i}",
        )
        for i in range(1, 11)
    ]

    def mock_run_agent(model, name, save_to=None, **kwargs):
        # Generate enough content to pass min_chars validation
        content = f"# {name} Output\n\n"
        content += f"This is the mocked content for the {name} agent.\n\n"
        content += "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        content += "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        content += "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. "
        content += "Nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
        content += "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla. "
        content += "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui "
        content += "officia deserunt mollit anim id est laborum.\n\n"
        content += f"## Summary for {name}\n\nThis completes the {name} phase output."
        if save_to:
            Path(save_to).parent.mkdir(parents=True, exist_ok=True)
            Path(save_to).write_text(content, encoding='utf-8')
        return content

    def mock_research_citations(output_path=None, **kwargs):
        # Create scout_raw.md file that research phase expects
        if output_path:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            scout_content = "## Scout Results\n\n"
            for i, c in enumerate(mock_citations, 1):
                scout_content += f"#### {i}. {c.title}\n**Authors**: {', '.join(c.authors)}\n**Year**: {c.year}\n\n"
            Path(output_path).write_text(scout_content, encoding='utf-8')
        return {'count': len(mock_citations), 'citations': mock_citations}

    mock_db = CitationDatabase(citations=mock_citations, citation_style="APA 7th")

    # CitationCompiler needs to be a class that returns an instance
    class MockCitationCompiler:
        def __init__(self, **kwargs):
            pass

        def generate_reference_list(self, draft):
            return "# References\n\n1. Author (2023). Mock Paper."

        def compile_citations(self, draft, **kwargs):
            return (draft, ["cite_001"], [])

    mock_compiler = MockCitationCompiler

    def mock_export_pdf(md_file=None, output_pdf=None, **kwargs):
        """Mock PDF export - creates the output file."""
        if output_pdf:
            Path(output_pdf).parent.mkdir(parents=True, exist_ok=True)
            Path(output_pdf).write_text("Mock PDF content", encoding='utf-8')
        return True

    def mock_export_docx(md_file=None, output_docx=None, **kwargs):
        """Mock DOCX export - creates the output file."""
        if output_docx:
            Path(output_docx).parent.mkdir(parents=True, exist_ok=True)
            Path(output_docx).write_text("Mock DOCX content", encoding='utf-8')
        return True

    # List of patches to apply
    patches = [
        ('phases.research.research_citations_via_api', mock_research_citations),
        ('phases.research.run_agent', mock_run_agent),
        ('phases.structure.run_agent', mock_run_agent),
        ('phases.compose.run_agent', mock_run_agent),
        ('phases.validate.run_agent', mock_run_agent),
        ('utils.deduplicate_citations.deduplicate_citations', (mock_citations, {})),
        ('utils.scrape_citation_titles.TitleScraper', MagicMock()),
        ('utils.scrape_citation_metadata.MetadataScraper', MagicMock()),
        ('utils.citation_database.save_citation_database', MagicMock()),
        ('utils.citation_quality_filter.CitationQualityFilter', MagicMock()),
        ('utils.citation_database.load_citation_database', mock_db),
        ('utils.export_professional.export_pdf', mock_export_pdf),
        ('utils.export_professional.export_docx', mock_export_docx),
        ('utils.citation_compiler.CitationCompiler', mock_compiler),
        ('utils.abstract_generator.generate_abstract_for_draft', (True, "Abstract")),
        ('utils.agent_runner.rate_limit_delay', None),
        ('phases.research.rate_limit_delay', None),
        ('phases.structure.rate_limit_delay', None),
        ('phases.compose.rate_limit_delay', None),
        ('phases.validate.rate_limit_delay', None),
    ]

    with ExitStack() as stack:
        for target, return_value in patches:
            if callable(return_value) and not isinstance(return_value, (MagicMock, tuple)):
                stack.enter_context(patch(target, side_effect=return_value))
            else:
                stack.enter_context(patch(target, return_value=return_value))

        from draft_generator import generate_draft

        return generate_draft(
            topic=topic,
            language=language,
            academic_level=academic_level,
            output_dir=output_dir,
            output_type=output_type,
            skip_validation=True,
            verbose=verbose,
        )


def print_summary(results: List[TestResult]) -> None:
    """Print summary of all test results."""
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)

    passed = sum(1 for r in results if r.success)
    failed = sum(1 for r in results if not r.success)
    total_time = sum(r.duration_seconds for r in results)

    print(f"\nResults: {passed}/{len(results)} passed, {failed} failed")
    print(f"Total time: {total_time:.1f}s ({total_time/60:.1f} minutes)")

    print("\nDetails:")
    print("-" * 70)

    for r in results:
        status = "✅ PASS" if r.success else "❌ FAIL"
        print(f"  Test {r.topic_id}: {status} ({r.duration_seconds:.1f}s) - {r.topic[:40]}...")
        if not r.success:
            print(f"          Error: {r.error}")

    print("-" * 70)

    if failed > 0:
        print(f"\n⚠️  {failed} test(s) failed!")
        sys.exit(1)
    else:
        print(f"\n✅ All {passed} tests passed!")
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="E2E test runner for OpenDraft pipeline")
    parser.add_argument("--topic", type=int, help="Run only specific topic ID (1-5)")
    parser.add_argument("--mock", action="store_true", help="Use mocked LLM (no API calls)")
    parser.add_argument("--verbose", action="store_true", help="Show detailed output")
    parser.add_argument("--output-dir", type=str, default="/tmp/opendraft_e2e_tests",
                        help="Base output directory")

    args = parser.parse_args()

    output_base = Path(args.output_dir) / datetime.now().strftime("%Y%m%d_%H%M%S")
    output_base.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("OPENDRAFT E2E TEST RUNNER")
    print("=" * 70)
    print(f"Output directory: {output_base}")
    print(f"Mode: {'MOCK (no API calls)' if args.mock else 'LIVE (real API calls)'}")
    print("=" * 70)

    # Select topics to run
    if args.topic:
        topics = [t for t in TEST_TOPICS if t['id'] == args.topic]
        if not topics:
            print(f"Error: Topic {args.topic} not found. Valid IDs: 1-5")
            sys.exit(1)
    else:
        topics = TEST_TOPICS

    print(f"\nRunning {len(topics)} test(s)...")

    results = []
    for config in topics:
        result = run_test(
            config=config,
            output_base=output_base,
            verbose=args.verbose,
            mock=args.mock,
        )
        results.append(result)

    print_summary(results)


if __name__ == "__main__":
    main()
