# The cycle — grpc / federated

- source canon: `dojo/range-playbook.md`
- base technique: `dojo-range-playbook-the-cycle.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1550**
- context: **grpc** · auth **federated** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

1. catalog: what can be built (9 classes × flaw × seam × canon)
2. build: replica up on the lab port
3. strike: the family engines run their real probes against the replica
4. mirror: every confirmed strike becomes a kage rule — the lesson ends detected

## Probe adjustment (grpc × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
