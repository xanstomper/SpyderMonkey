# Shared 36-byte header (all kinds)

- source canon: `holyshit-mode/iceposeidon-binary-map-protocol.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
