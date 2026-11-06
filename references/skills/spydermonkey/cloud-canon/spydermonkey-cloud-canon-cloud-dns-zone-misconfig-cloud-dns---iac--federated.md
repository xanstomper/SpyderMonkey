# Cloud DNS Zone Misconfig (CLOUD-DNS-01) — iac / federated

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-dns-zone-misconfig-cloud-dns-.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- context: **iac** · auth **federated** · chain role **pivot**

## Context

- platform: template/state files are the infrastructure inventory — read-only crown of the exposure
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- class: public zone records pointing to deprovisioned services
- probe: the takeover engine — dangling record inventory
- wall: NO-GAIN

## Probe adjustment (iac × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
