# Shared 36-byte header (all kinds) — chain composition

- source canon: `holyshit-mode/iceposeidon-binary-map-protocol.md`
- base technique: `holyshit-mode-iceposeidon-binary-map-protocol-shared-36-byte.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| off | type | field |
|-----|------|-------|
| 0 | u8 | kind (1..8) |
| 1 | u8 | version = 1 |
| 2 | u16 LE | flags: 1=full, 1|2=clear, 4=sparse |
| 4 | u32 | generation (>0) |
| 8 | u32 | sequence (>0) |
| 12 | f64 | eventRevision |
| 20 | f64 | sampledAt (epoch ms, must be multiple of 100) |
| 28 | u16 | partIndex |
| 30 | u16 | partCount (1..256) |
| 32 | u16 | recordCount |
| 34 | u16 | reserved (must be 0) |

Sparse/clear semantics: sparse = patch upserts (recordCount>0), clear = empty replacement (recordCount=0, len==36).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
