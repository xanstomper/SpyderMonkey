# CORS arbitrary origin on Bearer-token APIs — config flaw, not direct exploit

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`access-control-allow-origin: https://evil.com` reflected on an OpenAI-compatible API is **only CVSS 9.1 if the API uses cookie-based auth**. When the API uses `Authorization: Bearer <token>` and the SPA stores tokens in `sessionStorage` / `localStorage`:

- A malicious cross-origin site CAN make fetch requests with `credentials: 'include'`
- But the browser will NOT attach the Bearer header (that's set by JS, not the browser)
- And sessionStorage is origin-scoped — the malicious site cannot read the victim's token

**Score this LOW/MEDIUM config flaw, not critical.** It only becomes exploitable when chained with a separate token-leak primitive (XSS, postMessage leak, referrer leak). Don't false-positive it the way l***REDACTED***.ai's cookie-auth CORS was a true 9.1.

Quick discriminator: check `Set-Cookie` on login / `WWW-Authenticate` header. If auth is Bearer-only and no session cookie is set, CORS reflection is informational.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
