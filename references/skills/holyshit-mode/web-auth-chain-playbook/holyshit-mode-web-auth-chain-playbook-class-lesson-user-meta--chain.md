# Class lesson: user_metadata persistence ≠ authorization — chain composition

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-class-lesson-user-meta.md`
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

Admin-claim injection into JWT `user_metadata` (role/is_admin/credits persist verbatim through
phone signup) is a finding only if a BACKEND endpoint trusts the claim. example-target.xyz's backend
gates on its own DB (`profiles.email_verified` middleware on all /api/account/*) — dead end
despite full claim persistence. Locate the real gate before scoring JWT-claim escalation.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
