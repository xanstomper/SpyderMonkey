# Negative Results (Coverage Evidence) — mobile-api / machine

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-negative-results-coverage-evid.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **mobile-api** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

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

## Probe adjustment (mobile-api × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
