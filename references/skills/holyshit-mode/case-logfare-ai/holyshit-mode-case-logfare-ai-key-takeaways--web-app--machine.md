# Key Takeaways — web-app / machine

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-key-takeaways.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **web-app** · auth **machine** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

1. **FastAPI `openapi.json` exposure** gave full endpoint map including undocumented SSO flow
2. **CORS test on all endpoints** revealed arbitrary origin reflection with credentials — always test beyond login
3. **Rate limiter inconsistency** between rapid sequential vs. malformed requests — test both patterns
4. **Discord OAuth state cookie** properly implemented (HS256 JWT, 10-min expiry, secure nonce)
5. **Uniform error messages** prevented user enumeration via API key format
6. **postMessage with `window.location.origin`** is correct — don't false-alarm
7. **Subdomain CORS differential** — main API vulnerable, subdomains safe

## Probe adjustment (web-app × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
