# Key Takeaways — api / federated

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-key-takeaways.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **api** · auth **federated** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

1. **FastAPI `openapi.json` exposure** gave full endpoint map including undocumented SSO flow
2. **CORS test on all endpoints** revealed arbitrary origin reflection with credentials — always test beyond login
3. **Rate limiter inconsistency** between rapid sequential vs. malformed requests — test both patterns
4. **Discord OAuth state cookie** properly implemented (HS256 JWT, 10-min expiry, secure nonce)
5. **Uniform error messages** prevented user enumeration via API key format
6. **postMessage with `window.location.origin`** is correct — don't false-alarm
7. **Subdomain CORS differential** — main API vulnerable, subdomains safe

## Probe adjustment (api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
