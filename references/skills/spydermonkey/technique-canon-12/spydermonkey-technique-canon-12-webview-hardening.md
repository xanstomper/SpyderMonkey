# WebView hardening

- source canon: `spydermonkey/technique-canon-12.md`
- bindings: **MASTG-PLATFORM** · **CWE-749** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

JS bridges/file-access/mixed-content classes. Decisive test: the bridge inventory + file-access flags = the rows.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
