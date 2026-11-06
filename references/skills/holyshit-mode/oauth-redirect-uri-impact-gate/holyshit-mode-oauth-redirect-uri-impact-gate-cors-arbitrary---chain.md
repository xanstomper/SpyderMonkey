# CORS arbitrary origin on Bearer-token APIs — config flaw, not direct exploit — chain composition

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- base technique: `holyshit-mode-oauth-redirect-uri-impact-gate-cors-arbitrary-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`access-control-allow-origin: https://evil.com` reflected on an OpenAI-compatible API is **only CVSS 9.1 if the API uses cookie-based auth**. When the API uses `Authorization: Bearer <token>` and the SPA stores tokens in `sessionStorage` / `localStorage`:

- A malicious cross-origin site CAN make fetch requests with `credentials: 'include'`
- But the browser will NOT attach the Bearer header (that's set by JS, not the browser)
- And sessionStorage is origin-scoped — the malicious site cannot read the victim's token

**Score this LOW/MEDIUM config flaw, not critical.** It only becomes exploitable when chained with a separate token-leak primitive (XSS, postMessage leak, referrer leak). Don't false-positive it the way l***REDACTED***.ai's cookie-auth CORS was a true 9.1.

Quick discriminator: check `Set-Cookie` on login / `WWW-Authenticate` header. If auth is Bearer-only and no session cookie is set, CORS reflection is informational.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
