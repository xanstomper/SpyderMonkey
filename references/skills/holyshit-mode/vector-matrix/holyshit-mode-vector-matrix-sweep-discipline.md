# SWEEP DISCIPLINE

- source canon: `holyshit-mode/vector-matrix.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- One decisive probe per cell. A negative result IS a result — log it as coverage evidence.
- Escalate only on signal. No blind CVE spam, no spray-and-pray.
- HOLY SHIT = confirmed cell with impact narrative + kill-chain position. Everything else
  is documented coverage.
- All probes respect the mandate scope gate: scoped targets only, non-destructive, revert
  map before any state change, disclosure path for anything outside own infrastructure.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
