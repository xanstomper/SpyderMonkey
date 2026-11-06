# Resource Development Develop Capabilities (T1587) — host / federated

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-resource-development-develop-capab.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **host** · auth **federated** · chain role **final**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- class: malware/exploit/cert development
- probe: the family's "capabilities" are validators and provers, never payloads
- wall: NO-GAIN — every shipped script is read-only toward the operator's targets

## Probe adjustment (host × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
