# Certificate-error tolerance

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **MASTG-PLATFORM** · **CWE-749** · **ATT&CK T1557**
- generated: 2026-11-06

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

App proceeds on invalid certs (WebView handler returning true). Decisive test: local MITM cert accepted on your build = the row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
