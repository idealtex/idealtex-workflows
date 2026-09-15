# Idealtex workflows

Reusable validation and image publication following Remnivo's main-branch SemVer pattern.

Applications supply `service_name` (`mono`, `web-admin`, `web-public`) and `scripts/ci.sh`. Pull requests validate without write permissions. A successful main push validates, reserves `vMAJOR.MINOR.PATCH`, and publishes `ghcr.io/idealtex/<repository>:<tag>`. If that commit is still the main branch head, it also updates `ghcr.io/idealtex/<repository>:latest` from the published versioned image. Merged `major/` branches bump major, `feature/` branches bump minor, and other changes bump patch. Legacy numeric tags establish the starting version.

Reruns reuse the same commit's version. An existing versioned image must have the matching OCI revision label and is never overwritten. A failed publication can leave a reserved Git tag; rerun that workflow to finish it. Updating `latest` also runs when the verified versioned image already exists, so a rerun can recover a failed alias update without rebuilding. Older commits skip `latest` to prevent stale reruns from moving development backward. The alias copies the existing manifest with [Buildx imagetools](https://docs.docker.com/reference/cli/docker/buildx/imagetools/create/); it does not rebuild the image.

DEV can select `latest`; PROD selects an explicit version tag. Both are deployed manually in Dokploy. Publishing a new `latest` does not update running containers; deploy the application again to pull it. There are no deployment webhooks or cross-repository version updates. Application callers use the built-in GitHub token; no release PAT is required.

Run `python3 tests/test_latest.py` to check alias promotion, stale-run handling and failure propagation without registry access.

HUMAN ACTIONS: publish and review this repository first, then pin application reusable-workflow references to its reviewed full commit SHA before merging the application migrations. Do not modify the excluded legacy version repository. Require protected main branches, passing validation, and review for workflow changes.
