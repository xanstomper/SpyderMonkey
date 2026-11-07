# Class lesson: re-read old negatives narrowly (2026-10-10) — chain composition

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-class-lesson-re-read-o.md`
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

"SMS OTP dead" (verify path) coexisted with phone SIGNUP autoconfirm returning full sessions.
Negatives are scoped to the exact endpoint probed, not the feature family — enumerate sibling
endpoints (signup vs verify vs recover vs magiclink) before declaring an auth feature dead.
Also: email delivery may be broken server-side (signup confirm + email-change + recover all
silently dropped; verify with a healthy public-inbox API like Mailinator v2 as control).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
