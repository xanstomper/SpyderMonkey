# Re-verified

- source canon: `holyshit-mode/case-logfare-reengagement2.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

- **CORS arbitrary-origin + credentials reflection** (score 72) on every endpoint including
  state-changers (`/v1/auth/regenerate-key`, `/v1/me/delete`). BUT: auth is now cookie-based and
  observed cookies ship `SameSite=Lax; HttpOnly; Secure` + path scoping → cross-site POSTs don't
  carry the session. **Exploitability downgraded 9.1 → ~7.1.** Lesson: the SAME finding changes
  severity when the auth model changes — re-rate exploitability, not just presence, on re-engage.
- `/openapi.json` full exposure (60+ routes, no security schemes).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
