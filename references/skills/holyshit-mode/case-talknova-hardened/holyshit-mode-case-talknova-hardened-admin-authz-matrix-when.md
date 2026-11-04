# Admin authz matrix (when admin endpoints are discovered)

- source canon: `holyshit-mode/case-talknova-hardened.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

- GET unauth → expect 401
- POST unauth → expect 401
- PATCH/DELETE unauth → expect 401
- IDOR by numeric ID (`/users/1`, `/grants/1`, `/custom-keys/1`) → expect 401
- Mass assignment probe (`{"plan":"max","is_admin":true}`) → expect 401 or validation error
- Rate-limit probe on login → note decay time (talknova: 30 min)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
