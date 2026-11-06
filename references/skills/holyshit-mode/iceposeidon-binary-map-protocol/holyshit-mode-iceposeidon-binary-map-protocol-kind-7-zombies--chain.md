# Kind 7 — zombies (record size 37: `Ki=16` UUID, `Nd=37`) — chain composition

- source canon: `holyshit-mode/iceposeidon-binary-map-protocol.md`
- base technique: `holyshit-mode-iceposeidon-binary-map-protocol-kind-7-zombies.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `o+0` u32 rosterSequence, `o+4` u32 slotsSequence, `o+8` f64 timeBase
- Per record: 16-byte UUID id, u16 ownerSlot, i32 expiresAtDelta (timeBase + v*100, gated by flag bit `$d`), f32 speedMps (gated `Wi`), u8 flags (top 3 bits reserved must be 0; `Ld`=guard), f32 leechIntervalSeconds, f32 leechRadiusM, u16 leechAmount.
- Roster ids must be strictly sorted (`Qu(a,b)<0`).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
