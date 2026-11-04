# 2. user_metadata injection (limited value)

- source canon: `holyshit-mode/web-llm-proxy-auth-bypasses.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- Arbitrary `user_metadata` (role, is_admin, credits) PERSISTS into the JWT via signup/update.
- Backends authorize on their own DB (`profiles` / `app_metadata`), NOT client metadata →
  admin bypass fails. Expect `email_not_verified` middleware on all privileged routes.
- Don't burn turns re-testing metadata escalation against a well-built backend.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
