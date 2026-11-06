# Modbus/S7/BACnet exposure classes — chain composition

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-modbus-s7-bacnet-exposure-cla.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Protocol banners reachable unauth (502/102/47808) — the BANNER is the inventory finding; control writes are the absolute wall (never sent). Decisive test: read-only identity/banners on in-scope industrial tiers.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
