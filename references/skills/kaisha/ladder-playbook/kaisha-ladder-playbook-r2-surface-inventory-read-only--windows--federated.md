# R2 — surface inventory (read-only) — windows / federated

- source canon: `kaisha/ladder-playbook.md`
- base technique: `kaisha-ladder-playbook-r2-surface-inventory-read-only.md`
- bindings: **MASTG-RES** · **CWE-798** · **ATT&CK T1552**
- context: **windows** · auth **federated** · chain role **pivot**

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- listening services: address:port + process name (own host)
- banners: exact strings → feed `kaisha cve --banner`

## Probe adjustment (windows × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
