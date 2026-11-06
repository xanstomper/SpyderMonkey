# Synthesis operators (sibling variants) — chain composition

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-synthesis-operators-sibling-variants.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
