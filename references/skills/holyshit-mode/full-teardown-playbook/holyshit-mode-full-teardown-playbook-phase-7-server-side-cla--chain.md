# PHASE 7 — SERVER-SIDE CLASS PROBES (scoped, minimal) — chain composition

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-phase-7-server-side-cla.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- SQLi class: error-based + boolean oracle on clearly-input-reflected params first.
- SSRF: webhook/URL-import features → internal addresses (169.254.169.254 metadata =
  HOLY SHIT: cloud creds).
- XXE/SSRF in document processors; deserialization in session/upload paths.
- Upload handling: content-type/type-confusion, path traversal in filenames.
- Template injection in mail/report generators.
- Discipline: one probe per class on the most-likely param, escalate only on signal.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
