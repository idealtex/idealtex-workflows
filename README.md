# Idealtex workflows

Reusable validation and image publication following Remnivo's main-branch SemVer pattern.

Applications supply `service_name` (`mono`, `web-admin`, `web-public`) and `scripts/ci.sh`. Pull requests validate without write permissions. A successful main push validates, reserves `vMAJOR.MINOR.PATCH`, and publishes `ghcr.io/idealtex/<repository>:<tag>`. Merged `major/` branches bump major, `feature/` branches bump minor, and other changes bump patch. Legacy numeric tags establish the starting version.

Reruns reuse the same commit's version. An existing image must have the matching OCI revision label and is never overwritten. A failed publication can leave a reserved Git tag; rerun that workflow to finish it.

DEV and PROD tags are selected and deployed manually in Dokploy. There are no deployment webhooks or cross-repository version updates. Application callers use the built-in GitHub token; no release PAT is required.

HUMAN ACTIONS: publish and review this repository first, then pin application reusable-workflow references to its reviewed full commit SHA before merging the application migrations. Do not modify the excluded legacy version repository. Require protected main branches, passing validation, and review for workflow changes.
