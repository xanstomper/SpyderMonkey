# The takeover loop (post-foothold cadence) — kubernetes / federated

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-the-takeover-loop-post-foot.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **kubernetes** · auth **federated** · chain role **final**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

```
primitive confirmed → OP-ESCALATE consumer hunt → foothold landed →
T1..T7 applicable battery → decisive proof → chain hop recorded →
re-score remaining expansion vectors (§14) → next hop or TAKEOVER certification
```
Negatives are hops too: a key that fails on the next host is ledgered with the exact
test — never re-probed without a target change (canon).

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
