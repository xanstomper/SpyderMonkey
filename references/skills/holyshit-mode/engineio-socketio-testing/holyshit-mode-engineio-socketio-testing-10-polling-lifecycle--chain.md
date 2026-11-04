# 10. Polling lifecycle + transport/CDN traps — chain composition

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-10-polling-lifecycle.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
