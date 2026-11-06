# T4 — Cloud account takeover — kubernetes / federated

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-t4-cloud-account-takeover.md`
- bindings: **WSTG-INPV-10** · **CWE-918** · **ATT&CK T1190**
- context: **kubernetes** · auth **federated** · chain role **final**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- Secret leak → `sts get-caller-identity` success in the target account; bucket/object
  keys → deeper IAM; metadata/SSRF → instance role credential (one `get-caller-identity`,
  owned infra only for the decisive call); exposed snapshot/AMI → root volume → secrets;
  OIDC federation misconfig (documented-PoC); over-scoped service principals.
- **DECISIVE PROOF:** the harvested identity resolves to the target account and lists
  one resource. Then STOP.

## Probe adjustment (kubernetes × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
