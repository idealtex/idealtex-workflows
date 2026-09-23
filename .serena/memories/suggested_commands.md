# Local command entry points
- Windows PowerShell workspace; prefer rg for file/non-code searches, git -C <repo> status --short and git -C <repo> diff --check for changes.
- Python launcher: py. Shell scripts require a Bash environment; use the repository's documented runner.
- Management validation from its checkout: bash scripts/validate.sh .env.example. It uses local Docker; inspect prerequisites first.
- Backend CI entry point: scripts/ci.sh. Read usage before invoking; database/integration checks require disposable local dependencies.
- Frontend scripts and pinned Node/npm versions are in each package.json; read scripts instead of guessing command names.
- Read-only gh queries are authorized. Never run gh mutations, git push or remote write commands on behalf of the user.
