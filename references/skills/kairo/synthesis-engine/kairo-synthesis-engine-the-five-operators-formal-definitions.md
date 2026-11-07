# The five operators — formal definitions

- source canon: `kairo/synthesis-engine.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Op | Transform | Example | Wall note |
|---|---|---|---|
| SEAM | same primitive, adjacent trust seam (C↔E, B↔F, L↔M) | BOUNDARY on auth↔backend → same swap at edgefn↔db | seam is canon; primitive unchanged |
| FAMILY | same primitive, sibling flaw family (6↔2, 5↔1, 10↔3, 17↔16, 18↔14) | identifier-trust → trust-in-client-params | flaw families are canon |
| ESCALATE | read→write proof class (accepted→granted, 200→grants) | replay proof → duplicate-grant proof | still validation-only, reversed after |
| MIRROR | invert the trust direction (the seam's other side) | server-trusts-client → client-trusts-server check | same test family, opposite side |
| TRANSPOSE | same primitive, different domain surface | web BOUNDARY → HWFLASH slot-id trust | see the domain map below |

Each op emits a CONCRETE variant: own id, technique, proof, Δ — never a note.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
