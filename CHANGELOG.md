# Changelog

All notable changes are documented in this file.

## 2026-02-16

### Added
- CI quality gate workflow: `.github/workflows/quality.yml`
- Maintainer push/auth runbook: `docs/MAINTAINER_PUSH_RUNBOOK.md`
- Automated push preflight checker: `scripts/push-preflight.sh`

### Changed
- Migrated Gemini runtime usage from legacy SDK to `google-genai` wrappers across engine modules.
- Replaced deprecated `google-generativeai` dependency pins with `google-genai>=1.0.0`.
- Stabilized pytest harness with strict markers and integration test separation.

### Fixed
- Output cleaning regression that could strip real references sections.
- Live factcheck integration tests now skip safely in offline/restricted environments.

### Verification
- `python3 -W error::SyntaxWarning -m compileall -q engine tests` passed.
- `python3 -m pytest tests -q` passed (`286 passed, 4 deselected`).
- Push preflight passed with clean sync and correct maintainer account.

### Commits
- `8d09aa8` migrate gemini runtime to google-genai
- `ffdb23c` fix output cleaning regressions and reference handling
- `2c09445` add quality gates and verified fixes log
- `b6dca5e` stabilize pytest harness for ticket and integration tests
- `acaa0d2` harden live factcheck tests for offline and restricted envs
- `31c2b57` add push preflight runbook and guard script
