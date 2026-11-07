# 3. Header/CRLF + stored-XSS sweep on the proxy + status/docs pages

- source canon: `holyshit-mode/compromise-vs-observation-and-hardened-gateway-reengagement.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- CRLF: `\r\n` and `%0d%0a` payloads in the model field; check for an injected header
  (e.g. `X-Evil`) in the response. A JSON-escaped error body (404 model_not_found echoing the
  payload escaped) = no header injection; log negative.
- Stored XSS: grep `/status` and `/docs` HTML for `innerHTML`, then read the template. The
  pattern `const esc = s => String(s??"").replace(/[&<>"']/g,...)` covering the injected
  field(s) = SAFE. `/v1/models` catalog being server-sourced (client can't add models) =
  no reachable stored XSS sink. Log `stored_xss_status_docs=negative`.
- CORS: `Origin: https://evil.com` on every endpoint (models, chat, status, docs, playground,
  health, pg/chat). NO `access-control-allow-origin` reflection + no `allow-credentials` +
  no `Set-Cookie` = no browser session compromise. Log `cors_credentials=negative`.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
