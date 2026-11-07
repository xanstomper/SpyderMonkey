# Gate analysis (the critical lesson) — chain composition

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- base technique: `holyshit-mode-supabase-gotrue-playbook-gate-analysis-the-cri.md`
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

A "verification required" (e.g. `email_not_verified`, `turnstile_required`) error on one endpoint is NOT a global gate. Fuzz sibling endpoints with the same session before concluding:
- `/api/account/*` may demand email verification while `/api/media/*` on the chat subdomain accepts the same unverified session.
- Text chat gated by server-side Turnstile ≠ media endpoints gated. Media (speech/images/transcriptions) often runs wide open.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
