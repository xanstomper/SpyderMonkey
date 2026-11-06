# Ghost-route discrimination — api / federated

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-ghost-route-discriminat.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **api** · auth **federated** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

404s returning `application/json` = real routing layer (not SPA fallback). Only `text/html`
404/200s are ghosts. Check `/openapi.json`, `/docs`, `/api/docs` — but expect them genuinely absent on hardened non-FastAPI targets.

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
