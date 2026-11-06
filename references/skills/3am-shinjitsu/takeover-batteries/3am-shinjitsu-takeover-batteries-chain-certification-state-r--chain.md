# Chain certification (state + report) — chain composition

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-chain-certification-state-r.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Campaign state `chains[]`: `{crown_jewel, steps, status, impact, evidence}`.
- `steps` written as `A→B→C` where each hop is a confirmed primitive.
- `status: TAKEOVER` only when the final hop's decisive proof LANDED.
- `status: PARTIAL` = primitive confirmed but the impact-gate is missing — name it.
- `status: BLOCKED` = the deck stops here (auth, vantage, wall) — name the exact gap.
Tooling: `python3 scripts/exploit-intel.py chain --target <t> --jewel <crown> \
--steps "A→B→C:TAKEOVER" --impact "<one line>"` — dedupes, renders in `report`.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
