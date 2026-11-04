# Kind 1 — contestant location fixes (record size 11)

- source canon: `holyshit-mode/iceposeidon-binary-map-protocol.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
