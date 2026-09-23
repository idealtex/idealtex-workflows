# idealtex-workflows

# Idealtex workspace
- Multi-repository migration workspace; inspect each checkout's status/default branch before editing. Some project repositories may not be cloned locally.
- User authorizes local preparation and read-only SSH/GitHub inspection. All SSH/GitHub mutations, pushes, deployments, DNS/provider changes belong to HUMAN ACTIONS. Do not touch idealtex-releases.
- Prefer DproVision management and Remnivo publication patterns. Application repositories publish versioned images; humans choose deployed tags in Dokploy.
- Architecture/reference locations: `mem:tech_stack`. Operational commands: `mem:suggested_commands`. Editing constraints: `mem:conventions`. Verification/handoff: `mem:task_completion`.
- Current host inventory and checkpoints live in idealtex-management/HUMAN_ACTIONS.md, EXECUTION_STATUS.md and dated inspection reports; re-read instead of relying on remembered IPs or completion status.

- Workspace paths naming another repository refer to a sibling checkout; do not assume those files are present in a standalone clone.
