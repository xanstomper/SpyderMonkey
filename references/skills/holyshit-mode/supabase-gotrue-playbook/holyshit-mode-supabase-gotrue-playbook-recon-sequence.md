# Recon sequence

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

1. `GET /auth/v1/settings` with anon key reveals `phone_autoconfirm`, `mailer_autoconfirm`, enabled providers. `phone_autoconfirm:true` = POST `/auth/v1/signup` with `{phone, password}` returns a FULL confirmed session (access+refresh JWT, no OTP). This is the master key — mint unlimited accounts in seconds.
2. Mine all SPA bundles (main + lazy chunks) for the real API route table — actual surface (`/api/account/session`, `/api/auth/platform-handoff/*`, `/api/media/*`) differs from advertised docs.
3. Probe all subdomains found in handoff `redirectUrl`s (chat.*, platform.*, etc.) — each has its own API surface and often weaker gates.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
