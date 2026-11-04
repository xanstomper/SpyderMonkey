# Handoff-code entropy — unbruteforceable to size blind

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

A one-time handoff code exchanged at `/api/auth/platform-handoff/exchange` (code → Supabase access+refresh tokens) is a juicy target, but you CANNOT size its entropy without observing one real code. Uniform `401 invalid_handoff_code` on garbage gives no format/length oracle. The `/start` endpoint requires a valid refresh_token to mint a code — pre-auth you can't generate one.

Log it as "brute surface open, entropy unknown" and move on. Sizing needs one authenticated session to trigger a real handoff and observe the code format in the redirect URL.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
