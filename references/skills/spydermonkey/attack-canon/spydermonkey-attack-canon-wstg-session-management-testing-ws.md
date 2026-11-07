# WSTG Session Management Testing (WSTG-SESS)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: cookie flags, session fixation, logout, timeout
- probe: the SESSION battery (sequential ids) + cookie attribute inventory
- wall: read-only; fix=secure flags in the report

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
