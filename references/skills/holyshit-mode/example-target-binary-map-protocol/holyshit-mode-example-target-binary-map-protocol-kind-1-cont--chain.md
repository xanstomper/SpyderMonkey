# Kind 1 — contestant location fixes (record size 11) — chain composition

- source canon: `holyshit-mode/example-target-binary-map-protocol.md`
- base technique: `holyshit-mode-example-target-binary-map-protocol-kind-1-cont.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Layout after header (offsets are absolute, `o=36`, `l=recordCount`):
- `o+0` u32 definitionSequence (>0)
- `o+4` f64 ageBaseMs (epoch ms, grid of 100)
- `o+12` i32 latBase (scale 1e5, i.e. value/1e5 = degrees)
- `o+16` i32 lngBase (scale 1e5)
- `o+20` per-record i16 latDelta  (lat = (latBase + delta)/1e5)
- `o+20+l*2` per-record i16 lngDelta
- `o+20+l*4` per-record u16 slot
- `o+20+l*6` per-record u8 flags (bit1 = mock, bit2 = has age)
- `o+20+l*8` per-record u16 accuracyM (divide by 10 → meters)
- `o+20+l*10` per-record u16 ageSecondsAgo (at = ageBaseMs − v*100)

Example decode: header `01 01 01 00 ...`, latBase=3025493 lngBase=-9773031 → contestants slots 21/27/67 at lat 30.25479–30.25508, lng -97.73009…-97.73053.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
