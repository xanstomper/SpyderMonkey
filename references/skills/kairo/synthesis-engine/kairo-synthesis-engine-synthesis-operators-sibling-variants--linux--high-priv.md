# Synthesis operators (sibling variants) — linux / high-priv

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-synthesis-operators-sibling-variants.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **linux** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (linux × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
