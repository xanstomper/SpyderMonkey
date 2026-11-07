# Gate analysis (the critical lesson)

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

A "verification required" (e.g. `email_not_verified`, `turnstile_required`) error on one endpoint is NOT a global gate. Fuzz sibling endpoints with the same session before concluding:
- `/api/account/*` may demand email verification while `/api/media/*` on the chat subdomain accepts the same unverified session.
- Text chat gated by server-side Turnstile ≠ media endpoints gated. Media (speech/images/transcriptions) often runs wide open.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
