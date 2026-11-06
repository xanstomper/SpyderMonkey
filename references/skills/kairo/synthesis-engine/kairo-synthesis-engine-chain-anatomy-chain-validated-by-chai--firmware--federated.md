# Chain anatomy (`chain`, validated by `chain --validate`) — firmware / federated

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-chain-anatomy-chain-validated-by-chai.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **firmware** · auth **federated** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- Hops play roles: **entry** (AUTHBYPASS/ENTITLEMENT, order 0) → **mid**
  (BOUNDARY/REPLAY/STATEBYPASS/HDRADIO, order 1–2) → **value** (MATH/HWFLASH, order 3).
- The final hop MUST carry an impact gate — its decisive proof is what flips the
  chain to TAKEOVER; without the gate the chain is a PARTIAL (a named gap).
- `chain --validate` checks: every hop id exists in the vector pool · ordering
  respects entry→mid→value · final hop gated. Any failure → exit 1 with the
  broken chain list. Chains are emitted in 3AM format (`A→B→C:TAKEOVER`).

## Probe adjustment (firmware × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
