# Results (negatives are results — log them)

- source canon: `holyshit-mode/case-talknova-hardened.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

- CORS arbitrary origin+credentials: NEGATIVE (hard origin lock on all cookie endpoints).
- OAuth state/PKCE/open-redirect/replay: NEGATIVE (textbook hardening).
- Rate limiting on /api/admin/login: CONFIRMED WORKING (4 fails → 429, 30-min decay).
- Authz on admin surface: NEGATIVE (all endpoints 401 without session).
- IDOR on admin user/grant/custom-key endpoints: NEGATIVE (401 on all unauth attempts).
- SQLi/NoSQLi on admin login: NOT TESTED (rate limiter locked us out first).
- Ghost routes: all /api 404s are `application/json` — real routing.
- Backdoors: no client-side ID hardcodes or role gates in the bundle.
- CSP: hash/nonce lockdown; no obvious XSS delivery channel.
- API key auth: NEGATIVE (/v1/models 401 without Bearer).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
