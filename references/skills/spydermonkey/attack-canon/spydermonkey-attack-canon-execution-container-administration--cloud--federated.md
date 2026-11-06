# Execution Container Administration Command (T1609) — cloud / federated

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-execution-container-administration.md`
- bindings: **PTES-CON** · **CWE-250** · **ATT&CK T1611**
- context: **cloud** · auth **federated** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- class: exec into running containers
- probe: read-only inventory of the container surface; NO exec
- wall: REFUSED — namespace escape execution is outside every wall

## Probe adjustment (cloud × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
