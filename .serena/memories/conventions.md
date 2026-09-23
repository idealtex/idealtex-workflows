# Readability
- Avoid comments unless they identify a danger, subtle constraint, or potential problem.
- Write exception messages in English.
- Keep readable line breaks and blank lines; split distinct workflows into functions instead of repeating conditions.
- Follow the repository's language and formatter conventions. These conventions take precedence over Ponytail when they conflict.

# Publication conventions
- Pull-request validation has read-only permissions and does not publish images.
- Reuse the same version for reruns of the same commit. Never overwrite an existing versioned image; verify its OCI revision label.
- Promote `latest` only when the published commit is still the main-branch head; older reruns must not move it backward.
- Publish images only; no deployment webhooks or cross-repository version updates. Do not modify idealtex-releases.
- Application callers pin reusable workflows to a reviewed full commit SHA.

# Editing boundaries
- Preserve unrelated changes and reuse this repository's existing patterns.
- Keep credentials out of source, reports, command arguments and outputs; record environment variable names, not secret values.
- Do not commit or push unless explicitly requested. Do not execute SSH write commands or GitHub mutations through gh. Remote deployment and provider changes remain HUMAN ACTIONS.
- Keep validation artifacts in ignored local output directories; publish only reviewed, sanitized documentation.
