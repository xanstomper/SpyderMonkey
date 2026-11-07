# PHASE 7 — SERVER-SIDE CLASS PROBES (scoped, minimal)

- source canon: `holyshit-mode/full-teardown-playbook.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- SQLi class: error-based + boolean oracle on clearly-input-reflected params first.
- SSRF: webhook/URL-import features → internal addresses (169.254.169.254 metadata =
  HOLY SHIT: cloud creds).
- XXE/SSRF in document processors; deserialization in session/upload paths.
- Upload handling: content-type/type-confusion, path traversal in filenames.
- Template injection in mail/report generators.
- Discipline: one probe per class on the most-likely param, escalate only on signal.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
