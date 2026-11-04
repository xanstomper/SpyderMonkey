# Kind 7 — zombies (record size 37: `Ki=16` UUID, `Nd=37`)

- source canon: `holyshit-mode/i***REDACTED***-binary-map-protocol.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## The technique

- `o+0` u32 rosterSequence, `o+4` u32 slotsSequence, `o+8` f64 timeBase
- Per record: 16-byte UUID id, u16 ownerSlot, i32 expiresAtDelta (timeBase + v*100, gated by flag bit `$d`), f32 speedMps (gated `Wi`), u8 flags (top 3 bits reserved must be 0; `Ld`=guard), f32 leechIntervalSeconds, f32 leechRadiusM, u16 leechAmount.
- Roster ids must be strictly sorted (`Qu(a,b)<0`).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
