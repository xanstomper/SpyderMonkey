# CORS arbitrary origin on Bearer-token APIs — config flaw, not direct exploit — gateway / high-priv

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- base technique: `holyshit-mode-oauth-redirect-uri-impact-gate-cors-arbitrary-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **gateway** · auth **high-priv** · chain role **pivot**

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

`access-control-allow-origin: https://evil.com` reflected on an OpenAI-compatible API is **only CVSS 9.1 if the API uses cookie-based auth**. When the API uses `Authorization: Bearer <token>` and the SPA stores tokens in `sessionStorage` / `localStorage`:

- A malicious cross-origin site CAN make fetch requests with `credentials: 'include'`
- But the browser will NOT attach the Bearer header (that's set by JS, not the browser)
- And sessionStorage is origin-scoped — the malicious site cannot read the victim's token

**Score this LOW/MEDIUM config flaw, not critical.** It only becomes exploitable when chained with a separate token-leak primitive (XSS, postMessage leak, referrer leak). Don't false-positive it the way l***REDACTED***.ai's cookie-auth CORS was a true 9.1.

Quick discriminator: check `Set-Cookie` on login / `WWW-Authenticate` header. If auth is Bearer-only and no session cookie is set, CORS reflection is informational.

## Probe adjustment (gateway × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
