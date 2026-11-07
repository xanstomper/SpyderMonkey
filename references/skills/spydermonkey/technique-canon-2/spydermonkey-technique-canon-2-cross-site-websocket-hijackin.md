# Cross-site WebSocket hijacking (CSWSH)

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-06

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

WS handshake rides cookies without Origin checking — a page YOU control opens the socket with the victim's session. Decisive test: your own two-browser harness — Origin=evil.example accepted = the class (your own principal on both sides).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
