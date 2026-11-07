# Subprotocol/namespace confusion

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-CLNT-05** · **CWE-345** · **ATT&CK T1557**
- generated: 2026-11-06

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`Sec-WebSocket-Protocol` and socket.io namespace gates answering when they should not. Decisive test: the anon namespace CONNECT ack (type-matched to the app) = the exposure class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
