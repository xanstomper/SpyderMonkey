# Employee/artifact-string exposure (zero-document boundary)

- source canon: `spydermonkey/technique-canon-5.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-06

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Public artifact strings (git emails, doc metadata) — barbican's protect/sanitize canon applied OFFENSIVELY as recon: what does the ESTATE leak about itself. Decisive test: the string source URL — each leak is a row. Zero-document rule: no people-targeting, estate-artifacts only.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
