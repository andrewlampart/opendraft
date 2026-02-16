# OpenDraft v1 - Fixes Needed (Verified)

Date: 2026-02-16
Scope: `/Users/federicodeponte/opendraft`

## Verification Snapshot
- `pytest engine/tests -q` -> `108 passed, 10 skipped, 1 warning`.
- `python3 -W error::SyntaxWarning -m py_compile engine/utils/pdf_engines/pandoc_engine.py` fails with invalid escape sequence at line 209.
- `rg -n "google\\.generativeai" engine | wc -l` -> `11` matches in engine code.
- `.github/workflows` directory is absent (no CI workflow files in this repo snapshot).

## 1) Replace deprecated Gemini SDK import
- Severity: Medium
- File: `engine/utils/agent_runner.py:45`
- Current code: `import google.generativeai as genai`
- Evidence: pytest emits a deprecation warning that support for `google.generativeai` has ended.
- Fix:
  - Migrate to `google.genai` client usage across the runner path.
  - Update dependency pins/docs to reflect only the maintained SDK.

## 2) Remove invalid escape sequence in Pandoc engine docstring text
- Severity: Medium
- File: `engine/utils/pdf_engines/pandoc_engine.py:209`
- Current text contains `\maketitle` in a normal string/docstring context and triggers `SyntaxWarning: "\\m" is an invalid escape sequence`.
- Fix:
  - Escape the backslash (`\\maketitle`) or use a raw string for that block.
  - Keep `python3 -W error::SyntaxWarning -m py_compile engine/utils/pdf_engines/pandoc_engine.py` green in CI.

## 3) Complete SDK migration across remaining engine references
- Severity: Medium
- Evidence: `google.generativeai` references are still present in these engine files:
  - `engine/draft_generator.py:46`
  - `engine/utils/deep_research.py:54`
  - `engine/utils/api_tier_detector.py:13`
  - `engine/utils/citation_compiler.py:12`
  - `engine/utils/token_counter.py:78`
  - `engine/utils/api_citations/orchestrator.py:1289`
  - `engine/generate_thesis_tracked.py:36`
  - `engine/generate_thesis_tracked.py:78`
  - `engine/opendraft/verify.py:29`
  - `engine/utils/agent_runner.py:45`
- Fix:
  - Migrate remaining runtime imports to `google.genai`.
  - Keep backward-compat wrapper only where required for transitional code.

## 4) Update dependency metadata away from deprecated SDK
- Severity: Medium
- Files:
  - `requirements.txt:8`
  - `engine/requirements.txt:7`
  - `engine/pyproject.toml:44`
- Current dependency pin uses `google-generativeai`.
- Fix:
  - Move dependencies to `google-genai`.
  - Align install docs and verification checks with the new SDK name.

## 5) Add regression automation for warnings and SDK path
- Severity: Medium
- Evidence: no `.github/workflows` directory exists in this repository snapshot.
- Fix:
  - Add a CI check that fails on `SyntaxWarning` in project modules.
  - Add a smoke test for runner initialization on the new SDK path.
  - Run `pytest engine/tests -q` as a required CI check.
