# Architecture snapshot (2026-10-04) — chain composition

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-architecture-snapshot-2.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Static SPA bundle at `/v2/index-DwftPOeS.js` (1.4MB) holds route table; page chunks:
  - `ApiAccessPage-R65e4e7N.js` — key CRUD UI
  - `AdminPage-Cgkb504W.js` — full admin portal UI
  - `PayPage-8GPU0X34.js` — manual crypto checkout (no wallet addresses client-side)
  - `DocsPage-B3El2gVm.js` — documentation
- Origin lock on all cookie-auth POSTs: wrong/missing/`null` Origin →
  `403 {"error":"Cross-origin request rejected."}`.
- OAuth: 10-min HttpOnly SameSite=Lax state cookie (`koda_oauth_state`) bound 1:1 to the state
  param, PKCE S256 with server-held verifier, hardcoded redirect_uri, `returnTo` sanitized.
- CSP: hash-based `script-src 'self'` + strict `connect-src` allowlist, `frame-ancestors 'none'`, COOP/CORP, HSTS.
- API keys: personal keys shared with web chat usage; admin can issue standalone keys with dollar balance + model allowlist.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
