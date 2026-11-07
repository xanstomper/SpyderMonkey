# T+8 — surface map (bounded, ≤20 req)

- source canon: `3am-shinjitsu/arsenal-index.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| # | Probe | Test | Confirmed-when |
|---|---|---|---|
| 10 | OpenAPI/docs | `curl -s -o /dev/null -w '%{http_code} %{content_type}' /openapi.json /docs /redoc /swagger.json /api-docs` | JSON 200 = full route map free |
| 11 | Ghost-route sweep | same command, pair status+content-type | `text/html` on JSON API path = SPA ghost / Access wall — classify, never verdict |
| 12 | CORS matrix | `curl -s -D - -o /dev/null -H 'Origin: https://evil.com' <each state-changing endpoint>` | ACAO reflection + `allow-credentials: true`; then read Set-Cookie SameSite before rating (`arsenal-03` §2.x) |
| 13 | security.txt | `curl /.well-known/security.txt` | bounty channel exists or deliverable = disclosure package |
| 14 | Health/IP-echo | `curl /api/health /health /status?json=1` | env flags, client_ip SSRF oracle, hidden-model map |
| 15 | TLS SAN | `openssl s_client -connect <host>:443 -servername <host> </dev/null 2>/dev/null \| openssl x509 -noout -ext subjectAltName` | hosts absent from DNS+bundle; JSON 404 on SAN host = live router |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
