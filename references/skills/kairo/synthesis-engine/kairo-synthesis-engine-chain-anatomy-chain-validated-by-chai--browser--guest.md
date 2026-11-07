# Chain anatomy (`chain`, validated by `chain --validate`) — browser / guest

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-chain-anatomy-chain-validated-by-chai.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **browser** · auth **guest** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- Hops play roles: **entry** (AUTHBYPASS/ENTITLEMENT, order 0) → **mid**
  (BOUNDARY/REPLAY/STATEBYPASS/HDRADIO, order 1–2) → **value** (MATH/HWFLASH, order 3).
- The final hop MUST carry an impact gate — its decisive proof is what flips the
  chain to TAKEOVER; without the gate the chain is a PARTIAL (a named gap).
- `chain --validate` checks: every hop id exists in the vector pool · ordering
  respects entry→mid→value · final hop gated. Any failure → exit 1 with the
  broken chain list. Chains are emitted in 3AM format (`A→B→C:TAKEOVER`).

## Probe adjustment (browser × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
