# Kind 3 — object positions (record size 20) — chain composition

- source canon: `holyshit-mode/i***REDACTED***-binary-map-protocol.md`
- base technique: `holyshit-mode-i***REDACTED***-binary-map-protocol-kind-3-object-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`o+0` u32 definitionSequence; `o+4` i32 latBase, `o+8` i32 lngBase (scale 1e5); then `o+12` l× i16 latDelta, then l× i16 lngDelta, then l× 16-byte UUID (lowercased id).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
