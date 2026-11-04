# Kind 4 — variable-length records (`en`-byte records, type table `Zd`)

- source canon: `holyshit-mode/iceposeidon-binary-map-protocol.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

`recordCount` from header; each record: first byte indexes table `Zd`, followed by typed fields via `Zd[r.getUint8(...)]` descriptor. (Not fully enumerated — event was quiet.)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
