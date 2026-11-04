# The alias policy (v1.2 — `alias`)

- source canon: `barbican/protection-playbook.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

- Derivation: `ghost-` + first 6 hex of sha256(`target#epoch`) — deterministic
  per target+epoch, stable across sessions, no randomness to lose.
- Rotation: `--rotate` bumps the epoch → new alias per engagement window. The
  posture's `--alias` (human-chosen) always wins over the derived suggestion.
- Artifacts carry the alias, NEVER the operator identity — and `sanitize` is the
  enforcement pass that makes it true on disk.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
