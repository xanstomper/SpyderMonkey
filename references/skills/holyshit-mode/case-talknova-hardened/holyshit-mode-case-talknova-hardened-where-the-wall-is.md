# Where the wall is

- source canon: `holyshit-mode/case-talknova-hardened.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

Everything interesting sits behind:
1. **Google session** — /api/chat plan-tier tampering, /api/usage IDOR, /api/apikey authz (can user A read user B's key?)
2. **Admin session** — admin API depth, session fixation, CSRF on state-changing admin POSTs, privilege escalation via mass assignment on /api/admin/users/:id

Pre-auth surface exhausted. The next decisive test REQUIRES credentials.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
