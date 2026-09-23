# C# code style
- Use Allman braces for all C# control blocks (if, else, loops, switch, try, catch, finally, using, and lock), matching the default .NET formatter. Put opening braces on a new line; keep body statements and closing braces on separate lines. Always use braced bodies, even for a single statement.
- Avoid code comments unless they identify a danger, subtle constraint, or potential problem.
- Always write exception messages in English. Never use Ukrainian or Russian text for exception messages.
- These code style rules take precedence over the Ponytail skill when they conflict; do not compress control blocks or sacrifice readability for fewer lines.
- Add line breaks and blank lines where appropriate to make code easier for humans to read.
- Split code into methods at logical responsibility boundaries. Dispatch to the appropriate method once instead of repeating the same condition throughout a method; keep each distinct workflow and its checks together.

# Editing invariants
- Store all flat (plain data-only) C# classes and records in the Idealtex.Mono.Entities project under the relevant domain namespace; do not declare these DTOs inside services, handlers, or other projects.
- Keep fixes local and minimal; reuse existing DproVision/Remnivo-derived patterns.
- EF must generate migrations and snapshots. Never hand-edit migration content; ask the user if EF generation is not possible.
- Preserve unrelated branches/changes; do not merge older monitoring work wholesale. Read EXECUTION_STATUS.md for selected/deferred changes.
- Keep credentials out of source, reports, arguments and outputs. Read approved environment variables only as needed; record names, not secret values.
- Use neutral manager/worker names and explicit placement for local state. Dokploy owns application tag selection; pipelines must not update idealtex-releases.
- Raw validation/inventory artifacts belong in ignored .validation; publish only reviewed sanitized documentation.
