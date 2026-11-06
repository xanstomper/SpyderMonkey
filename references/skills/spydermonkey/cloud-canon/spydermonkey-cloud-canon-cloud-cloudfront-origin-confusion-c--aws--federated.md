# Cloud CloudFront Origin Confusion (CLOUD-EDGE-01) — aws / federated

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-cloudfront-origin-confusion-c.md`
- bindings: **WSTG-ADV-01** · **CWE-444** · **ATT&CK T1190**
- context: **aws** · auth **federated** · chain role **pivot**

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- class: origin that answers any Host — the edge/cache chain opener
- probe: Host-header differentials through the declared distribution
- wall: read-only; cache-poisoning classes are proven lab-side only

## Probe adjustment (aws × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
