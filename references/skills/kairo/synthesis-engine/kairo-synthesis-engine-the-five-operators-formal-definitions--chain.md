# The five operators — formal definitions — chain composition

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-the-five-operators-formal-definitions.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Op | Transform | Example | Wall note |
|---|---|---|---|
| SEAM | same primitive, adjacent trust seam (C↔E, B↔F, L↔M) | BOUNDARY on auth↔backend → same swap at edgefn↔db | seam is canon; primitive unchanged |
| FAMILY | same primitive, sibling flaw family (6↔2, 5↔1, 10↔3, 17↔16, 18↔14) | identifier-trust → trust-in-client-params | flaw families are canon |
| ESCALATE | read→write proof class (accepted→granted, 200→grants) | replay proof → duplicate-grant proof | still validation-only, reversed after |
| MIRROR | invert the trust direction (the seam's other side) | server-trusts-client → client-trusts-server check | same test family, opposite side |
| TRANSPOSE | same primitive, different domain surface | web BOUNDARY → HWFLASH slot-id trust | see the domain map below |

Each op emits a CONCRETE variant: own id, technique, proof, Δ — never a note.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
