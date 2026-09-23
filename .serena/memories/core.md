# Project map
- Reusable GitHub Actions validation and image-publication workflows under `.github/workflows/`.
- Application callers provide `service_name` (`mono`, `web-admin`, `web-public`) and their own `scripts/ci.sh`.
- Publication follows the existing Remnivo-style main-branch SemVer flow; deployment remains manual in Dokploy.
- Read README.md for publication/rerun contracts. Tooling: `mem:tech_stack`. Commands: `mem:suggested_commands`. Constraints: `mem:conventions`. Verification: `mem:task_completion`. Memory scope: `mem:memory_maintenance`.
