# 10. Polling lifecycle + transport/CDN traps

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- **Socket.io polling allows exactly ONE in-flight GET.** Every POST must be followed by a
  single long GET (hold up to pingInterval); a fresh POST while a GET is pending, or a burst
  of short-timeout GETs, kills the session with `{"code":1,"message":"Session ID unknown"}`.
  That error AFTER a successful handshake+connect = your own polling rhythm, not CDN
  affinity. A quiet long-poll (read timeout, no data) is NORMAL — reconnect and continue,
  don't score it as a failure.
- **`400 {"code":0,"message":"Transport unknown"}` on `transport=polling` = the server
  restricts transports (websocket-only), NOT a missing endpoint.** Go websocket-first;
  don't EIO-fish the path.
- **CDN blocks non-browser websocket UPGRADES (403 HTML on the upgrade request) while
  polling frames pass the same path.** When the upgrade 403s with an HTML body, run
  connects/joins/emits over polling frames instead of churning upgrade headers — python
  websocket-client fingerprints non-browser TLS no matter the header set.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
