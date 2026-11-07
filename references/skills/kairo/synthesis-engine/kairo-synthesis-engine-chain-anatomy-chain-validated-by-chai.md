# Chain anatomy (`chain`, validated by `chain --validate`)

- source canon: `kairo/synthesis-engine.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Hops play roles: **entry** (AUTHBYPASS/ENTITLEMENT, order 0) → **mid**
  (BOUNDARY/REPLAY/STATEBYPASS/HDRADIO, order 1–2) → **value** (MATH/HWFLASH, order 3).
- The final hop MUST carry an impact gate — its decisive proof is what flips the
  chain to TAKEOVER; without the gate the chain is a PARTIAL (a named gap).
- `chain --validate` checks: every hop id exists in the vector pool · ordering
  respects entry→mid→value · final hop gated. Any failure → exit 1 with the
  broken chain list. Chains are emitted in 3AM format (`A→B→C:TAKEOVER`).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
