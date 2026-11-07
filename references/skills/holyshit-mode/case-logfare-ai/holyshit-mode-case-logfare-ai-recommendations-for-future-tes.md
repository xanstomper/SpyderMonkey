# Recommendations for Future Testing

- source canon: `holyshit-mode/case-logfare-ai.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

1. Obtain valid API key for post-auth testing
2. Test IDOR on /v1/me/data with modified user ID
3. Test SSO confusion race condition
4. Test stored XSS in chat completions
5. Test CSRF on state-changing endpoints with session
6. **2026-10-09 session: CSRF bypass via Origin spoofing confirmed** — `Origin: https://logfare.ai` passes CSRF on `/connections/revoke`. Logout endpoint has NO CSRF check at all. Destructive endpoints exposed if Origin check is bypassed.
7. **2026-10-09 session: Cross-origin brute-force confirmed** — login 429 responses include CORS + retry-after, enabling browser-based password brute-force with timing sync.
8. **2026-10-09 session: OpenAPI full enumeration completed** — 60+ endpoints mapped, all checked for CORS. Destructive endpoints: `/v1/me/delete` (GDPR erase), `/connections/revoke`, `/v1/auth/regenerate-key`, `/v1/auth/logout` all have CORS + credentials.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
