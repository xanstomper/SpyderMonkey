# Chain anatomy (`chain`, validated by `chain --validate`) — android / low-priv

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-chain-anatomy-chain-validated-by-chai.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **android** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Hops play roles: **entry** (AUTHBYPASS/ENTITLEMENT, order 0) → **mid**
  (BOUNDARY/REPLAY/STATEBYPASS/HDRADIO, order 1–2) → **value** (MATH/HWFLASH, order 3).
- The final hop MUST carry an impact gate — its decisive proof is what flips the
  chain to TAKEOVER; without the gate the chain is a PARTIAL (a named gap).
- `chain --validate` checks: every hop id exists in the vector pool · ordering
  respects entry→mid→value · final hop gated. Any failure → exit 1 with the
  broken chain list. Chains are emitted in 3AM format (`A→B→C:TAKEOVER`).

## Probe adjustment (android × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
