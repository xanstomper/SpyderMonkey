# Kind 3 — object positions (record size 20)

- source canon: `holyshit-mode/example-target-binary-map-protocol.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`o+0` u32 definitionSequence; `o+4` i32 latBase, `o+8` i32 lngBase (scale 1e5); then `o+12` l× i16 latDelta, then l× i16 lngDelta, then l× 16-byte UUID (lowercased id).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
