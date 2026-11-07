# Hygiene

- source canon: `kairo/synthesis-engine.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Vectors are marked `distributed` after a supply drop — never double-shipped.
- EXHAUSTED findings never enter the queue (negatives don't synthesize).
- Every compiled attack inherits its source finding's P0 scope. No scope, no ship.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
