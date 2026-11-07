# Recipes that carried this engagement

- source canon: `holyshit-mode/case-gamdom-com.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- EIO=3 websocket-first handshake (`GET /socket.io/?EIO=3&transport=websocket`, NO sid → server
  mints over websocket; polling dies on CDN node affinity with `Session ID unknown`) — unlocked
  the REAL protocol and both top finds. v2 frames: connect `40/nsp`, events `42/nsp,["ev",args]`.
- CDP `Page.addScriptToEvaluateOnNewDocument` hooking `window.WebSocket` — post-load hooks miss
  the bundled client (constructor captured at module init). Idle sockets capture nothing: drive
  the UI (open chat / games) to generate traffic.
- Shadow-DOM form driving (Dynamic SDK widget): pierce shadow roots, native value setter +
  input/change events, REAL clicks on checkboxes (silent client validation blocks submit
  otherwise — `isValidAge` checkValidity was the hidden blocker).
- Schema-library extraction: all request shapes live in ONE util chunk; `snake_case` method
  names = API methods; enums defined as var-ternary chains (`(n=>(n.COINS="COINS",...)).
- CT logs → wayback → whois → PTR chain for forgotten-edge hunting; hackertarget hostsearch for
  passive DNS (found td.gamdom.com + incoming-callbacks.gamdom.com); banner-grab everything
  (MariaDB version, Exim version, SSH version = the age of the box in one call).
- Kernel-state caution in execute_code: variable collisions across cells produce phantom type
  errors ('str' has no .get) — fresh names per cell, read responses to EOF, never trust a parse
  of a truncated body.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
