# Recipes that carried this engagement — chain composition

- source canon: `holyshit-mode/case-gamdom-com.md`
- base technique: `holyshit-mode-case-gamdom-com-recipes-that-carried-this-enga.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
