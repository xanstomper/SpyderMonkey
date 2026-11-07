# Recon sequence — edge-node / expired

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- base technique: `holyshit-mode-supabase-gotrue-playbook-recon-sequence.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **edge-node** · auth **expired** · chain role **entry**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

1. `GET /auth/v1/settings` with anon key reveals `phone_autoconfirm`, `mailer_autoconfirm`, enabled providers. `phone_autoconfirm:true` = POST `/auth/v1/signup` with `{phone, password}` returns a FULL confirmed session (access+refresh JWT, no OTP). This is the master key — mint unlimited accounts in seconds.
2. Mine all SPA bundles (main + lazy chunks) for the real API route table — actual surface (`/api/account/session`, `/api/auth/platform-handoff/*`, `/api/media/*`) differs from advertised docs.
3. Probe all subdomains found in handoff `redirectUrl`s (chat.*, platform.*, etc.) — each has its own API surface and often weaker gates.

## Probe adjustment (edge-node × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
