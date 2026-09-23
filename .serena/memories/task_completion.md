# Verification and handoff
- Use relevant existing checks for changed behavior; docs/endpoint-only edits need diff checks and targeted consistency review, not a full integration rerun.
- Report what was verified and material limits. Hardware inventory is not a load test; KVM guest observations cannot establish dedicated physical resources or failure domains.
- Separate local preparation from remote execution. Label every user-executed mutation HUMAN ACTIONS; never claim unexecuted setup completed.
- Verify new SSH certificate login in a separate session before disabling passwords. Keep recovery-console access during hardening.
- Update authoritative runbooks/checkpoints; avoid stale duplicated task state in memories. Serena memory references can be checked with serena memories check.
