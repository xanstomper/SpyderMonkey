# T+8 — surface map (bounded, ≤20 req) — chain composition

- source canon: `3am-shinjitsu/arsenal-index.md`
- base technique: `3am-shinjitsu-arsenal-index-t-8-surface-map-bounded-20-req.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| # | Probe | Test | Confirmed-when |
|---|---|---|---|
| 10 | OpenAPI/docs | `curl -s -o /dev/null -w '%{http_code} %{content_type}' /openapi.json /docs /redoc /swagger.json /api-docs` | JSON 200 = full route map free |
| 11 | Ghost-route sweep | same command, pair status+content-type | `text/html` on JSON API path = SPA ghost / Access wall — classify, never verdict |
| 12 | CORS matrix | `curl -s -D - -o /dev/null -H 'Origin: https://evil.com' <each state-changing endpoint>` | ACAO reflection + `allow-credentials: true`; then read Set-Cookie SameSite before rating (`arsenal-03` §2.x) |
| 13 | security.txt | `curl /.well-known/security.txt` | bounty channel exists or deliverable = disclosure package |
| 14 | Health/IP-echo | `curl /api/health /health /status?json=1` | env flags, client_ip SSRF oracle, hidden-model map |
| 15 | TLS SAN | `openssl s_client -connect <host>:443 -servername <host> </dev/null 2>/dev/null \| openssl x509 -noout -ext subjectAltName` | hosts absent from DNS+bundle; JSON 404 on SAN host = live router |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
