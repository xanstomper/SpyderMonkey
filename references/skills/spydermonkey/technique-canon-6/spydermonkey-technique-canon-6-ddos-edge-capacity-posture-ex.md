# DDoS/edge-capacity posture (exposure row)

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Cap-absence classes (canon-II HTTP/2) — registered from edge config signals only, floods never fired.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
