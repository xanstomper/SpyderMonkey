# Negative Results (Coverage Evidence) — chain composition

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-negative-results-coverage-evid.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Vector | Result | Notes |
|--------|--------|-------|
| Mass assignment (`is_admin`, `tier:99`) | Blocked | Discord membership check (403) |
| JWT alg:none on state cookie | Rejected | HS256 enforced, secure nonce |
| Open redirect in Discord OAuth | Blocked | `redirect_uri` hardcoded server-side |
| NoSQL injection (`{"$gt":""}`) | Safe | SQLAlchemy/Postgres parameterization |
| Array injection (`email:["admin"]`) | Safe | Type validation |
| Path traversal (`../../../etc/passwd`) | 404 | FastAPI routing, no file serve |
| SSTI in error messages | Safe | No template reflection |
| GraphQL introspection | 404 | No GraphQL endpoint |
| SSRF via model param | Requires auth | Cannot test without valid API key |
| API key format enumeration | Safe | Uniform error message |
| Timing oracle (user enum) | No difference | 0.112s vs 0.110s — negligible |
| postMessage origin check | Correct pattern | `window.location.origin` = safe |
| Request smuggling | Blocked | nginx rejects |
| LDAP/XPath injection | Not implemented | — |
| Prototype pollution | No effect | — |
| Header injection (X-Admin, X-User-ID) | Ignored | — |
| Method override | 405 | — |
| Content-type confusion | 400 | — |
| Subdomain CORS | Not vulnerable | chat./rp. safe, only main API |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
