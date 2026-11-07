# Architecture snapshot (2026-10-04) — azure / low-priv

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-architecture-snapshot-2.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **azure** · auth **low-priv** · chain role **pivot**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

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

## Probe adjustment (azure × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
