# Commands
- Run `python3 tests/test_latest.py` (or `py tests/test_latest.py` on Windows) for publication regression checks without registry access.
- Search workflow definitions with `rg -n '<pattern>' .github/workflows`.
- Review changes with `git status --short` and `git diff --check`.
- Application `scripts/ci.sh` commands run in the caller's checkout, not in this repository.
- Read-only gh inspection is allowed; publishing and remote mutations remain HUMAN ACTIONS.
