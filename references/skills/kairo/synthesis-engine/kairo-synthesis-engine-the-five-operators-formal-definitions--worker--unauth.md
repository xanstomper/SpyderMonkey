# The five operators — formal definitions — worker / unauth

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-the-five-operators-formal-definitions.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **worker** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

| Op | Transform | Example | Wall note |
|---|---|---|---|
| SEAM | same primitive, adjacent trust seam (C↔E, B↔F, L↔M) | BOUNDARY on auth↔backend → same swap at edgefn↔db | seam is canon; primitive unchanged |
| FAMILY | same primitive, sibling flaw family (6↔2, 5↔1, 10↔3, 17↔16, 18↔14) | identifier-trust → trust-in-client-params | flaw families are canon |
| ESCALATE | read→write proof class (accepted→granted, 200→grants) | replay proof → duplicate-grant proof | still validation-only, reversed after |
| MIRROR | invert the trust direction (the seam's other side) | server-trusts-client → client-trusts-server check | same test family, opposite side |
| TRANSPOSE | same primitive, different domain surface | web BOUNDARY → HWFLASH slot-id trust | see the domain map below |

Each op emits a CONCRETE variant: own id, technique, proof, Δ — never a note.

## Probe adjustment (worker × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
