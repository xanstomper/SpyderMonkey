# 2. user_metadata injection (limited value)

- source canon: `holyshit-mode/web-llm-proxy-auth-bypasses.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Arbitrary `user_metadata` (role, is_admin, credits) PERSISTS into the JWT via signup/update.
- Backends authorize on their own DB (`profiles` / `app_metadata`), NOT client metadata →
  admin bypass fails. Expect `email_not_verified` middleware on all privileged routes.
- Don't burn turns re-testing metadata escalation against a well-built backend.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
