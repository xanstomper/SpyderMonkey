# Kind 8 — zombie leech schedule (`Pd=20, Dd=9, Ud=6`)

- source canon: `holyshit-mode/i***REDACTED***-binary-map-protocol.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `o+0` u32 rosterSequence, `o+4` f64 timeBase, `o+12` i32 latBase, `o+16` i32 lngBase (scale 1e5)
- l× u8 count + l× u16 index; per zombie: u16 slot, i16 latDelta, i16 lngDelta, u16 targetSlot, then count× {u16 leechSlot, i32 nextHitAtDelta*100ms}.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
