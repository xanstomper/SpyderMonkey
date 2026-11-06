# Cloud Metadata Service Exposure (CLOUD-SSRF-01) — gcp / federated

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-metadata-service-exposure-clo.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **gcp** · auth **federated** · chain role **pivot**

## Context

- platform: IAM/service-account surface — read-only enumeration
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- class: 169.254.169.254 reachable through an in-scope app — the SSRF crown
- probe: the SSRF battery's metadata targets — the differential proves the reach
- wall: proof-of-reach only; metadata contents beyond the marker are never dumped

## Probe adjustment (gcp × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
