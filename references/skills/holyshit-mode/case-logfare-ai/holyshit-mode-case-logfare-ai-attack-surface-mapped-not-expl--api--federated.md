# Attack Surface Mapped (Not Exploited) — api / federated

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-attack-surface-mapped-not-expl.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **api** · auth **federated** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- **IDOR on DSAR:** `/v1/me/data`, `/v1/me/delete` — need valid session
- **SSO confusion:** Race condition on `/v1/sso/approve` + `/v1/sso/token` — need valid session
- **Post-auth injection:** Stored XSS, CSRF — need valid session
- **Rate limit bypass:** `X-Forwarded-For` spoofing — not tested
- **Premium model access:** Tier 1 models require auth — no bypass found

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
