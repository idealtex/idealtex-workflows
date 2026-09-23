# Verification and handoff
- Run `python3 tests/test_latest.py` for publication logic changes; review workflow syntax, permissions and caller inputs for YAML changes.
- Confirm rerun behavior, immutable versioned images and protection against stale latest-tag promotion remain intact.
- Do not publish images, dispatch remote workflows or change application workflow pins as a local validation step.
- Use checks relevant to the change; memory/documentation-only edits need diff and consistency checks, not application builds.
- Report what was verified and any material limits. Label required user actions HUMAN ACTION; never claim unexecuted work is complete.
