# MASTG WebView JS Bridge (MASTG-PLATFORM-05)

- source canon: `spydermonkey/mobile-canon.md`
- bindings: **MASTG-PLATFORM** · **CWE-749** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: addJavascriptInterface exposing native to web content
- probe: static inventory + the lab webview loads the marker page
- wall: lab only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
