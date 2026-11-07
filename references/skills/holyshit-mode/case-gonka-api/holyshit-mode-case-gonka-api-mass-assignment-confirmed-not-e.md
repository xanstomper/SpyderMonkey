# Mass-assignment: confirmed, NOT exploitable (gate re-confirmed)

- source canon: `holyshit-mode/case-gonka-api.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `/auth/v1/signup` `data:{role:"admin",is_admin:true,balance:999999,tier:"enterprise"}`
  persists VERBATIM into `user_metadata`, survives email confirmation into the
  verified JWT. `app_metadata` stays clean (GoTrue protects it).
- Gate: PostgREST RLS ignores `user_metadata`; edge-function billing reads real
  `balances.credits_cents` — a 2000-token completion deducted −0.002 from the
  20¢ balance. No backend authorizes on `user_metadata.role`. Score ~55
  hardening note, not a holy shit.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
