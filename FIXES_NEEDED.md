# OpenDraft - Fixes Status (Verified)

Date: 2026-02-16  
Scope: `/Users/federicodeponte/opendraft`

## Verification Snapshot
- `python3 -W error::SyntaxWarning -m compileall -q engine tests` -> pass
- `python3 -m pytest tests -q` -> `286 passed, 4 deselected`
- Legacy SDK scan -> no `google.generativeai` imports and no `google-generativeai` dependency pins

## Resolved in This Pass

### 1) Legacy Gemini SDK runtime usage removed
- Runtime modules now use `google.genai` + shared wrapper:
  - `engine/utils/gemini_client.py`
  - `engine/utils/agent_runner.py`
  - `engine/utils/deep_research.py`
  - `engine/utils/api_tier_detector.py`
  - `engine/utils/token_counter.py`
  - `engine/utils/api_citations/orchestrator.py`
  - `engine/utils/citation_compiler.py`
  - `engine/draft_generator.py`
  - `engine/generate_thesis_tracked.py`

### 2) Deprecated dependency pins replaced
- Updated to `google-genai>=1.0.0` in:
  - `requirements.txt`
  - `engine/requirements.txt`
  - `engine/pyproject.toml`
  - `engine/opendraft.egg-info/requires.txt`
  - `engine/opendraft.egg-info/PKG-INFO`

### 3) CI regression automation added
- Added `.github/workflows/quality.yml` with:
  - Python compile gate (`compileall`, syntax warnings as errors)
  - Guard against deprecated Gemini imports
  - Guard against deprecated dependency pin
  - Full default pytest suite run (`python -m pytest tests -q`)

### 4) Output cleaning edge case fixed
- `clean_agent_output()` no longer strips real `## References` sections by metadata pass.
- Regression test added:
  - `tests/test_output_cleanliness.py::TestStripMetadata::test_preserve_real_references_section`

## Remaining Tracked Gaps
- None from this issue set.

## Remaining Validation Gap
- Live API integration scripts now execute with prerequisite-aware skip behavior:
  - `tests/test_live_crafter.py` (direct and module invocation)
  - `tests/audit_output.py` (direct and module invocation)
- Full live generation assertions remain environment-dependent (API key + outbound network required).
