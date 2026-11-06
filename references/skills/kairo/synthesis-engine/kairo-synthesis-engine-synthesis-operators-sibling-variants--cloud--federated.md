# Synthesis operators (sibling variants) — cloud / federated

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-synthesis-operators-sibling-variants.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **cloud** · auth **federated** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

| Op | Meaning | Example |
|---|---|---|
| SEAM | retarget the primitive across a different trust seam | boundary primitive on the API plane → same on the webhook plane |
| FAMILY | transpose to the sibling flaw family | scope-trust (6/C) → identifier-trust sibling (6/E) |
| ESCALATE | same primitive, higher-impact gate | read-proof → write-proof (still validation-only) |
| MIRROR | the same seam from the other side | client-trusts-server → server-trusts-client |
| TRANSPOSE | same primitive, different domain surface | checkout state bypass → booking state bypass |

Each op emits a SEPARATE, CONCRETE vector with its own id/technique/proof/Δ
(`--expand` or `forge --expand`). ESCALATE variants keep the no-gain wall: the
write/grant proof is executed once and reversed. Chains: entry-class vectors
(AUTHBYPASS/ENTITLEMENT) → mid (REPLAY/STATEBYPASS) → value (MATH) — emitted in
3AM chain format `A→B→C:TAKEOVER`, TAKEOVER-CANDIDATE until the final hop's
decisive proof lands.

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
