# WSTG-CLNT-12 WebSocket Hijack

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **WSTG-CLNT-05** · **CWE-345** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: ws endpoints without origin checks
- probe: origin header differential on the lab ws endpoint
- wall: lab replica

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
