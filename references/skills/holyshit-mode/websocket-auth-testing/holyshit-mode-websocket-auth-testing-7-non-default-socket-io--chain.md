# 7. Non-default socket.io parsers: the msgpack silent-drop — chain composition

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-7-non-default-socket-io.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Some servers run `socket.io-msgpack-parser` — every TEXT frame (`40`, `42[...]`) is
silently dropped with NO ack and NO error, which reads exactly like an auth gate that
isn't one. Text `40` connects and msgpack connects can both be silently ignored while
the REAL client works. Discriminate by capture, never by frame-guessing:

- **Capture the real client first**: CDP `Network.enable` BEFORE `Page.navigate`, then
  collect `Network.webSocketFrameSent/Received` — CDP delivers bytes base64-encoded;
  decode with `msgpack.unpackb`. Connect = `{type:0, data:{}, nsp:"/ns"}` (data = EMPTY
  MAP, not nil), events = `{type:2, data:[name,args], nsp}`. Server acks carry a `pid`
  msgpack ext.
- **Frame injection onto the trusted socket beats replica sockets**: wrap
  `WebSocket.prototype.send` + a message listener via
  `Page.addScriptToEvaluateOnNewDocument`, then send hand-rolled msgpack bytes through
  the SPA's own live connection. Replica sockets with byte-identical frames and cookies
  can get CLOSED ~1s after the first packet (connection-level gate the replica lacks —
  TLS fingerprint or a registration the SPA did at load); frames injected onto the
  trusted connection are processed normally.
- **Protocol violations kill the connection SILENTLY**: an EVENT on a namespace never
  CONNECTed, or any malformed packet — no error frame, the socket just stops answering.
  After any violation RELOAD the page; never re-probe on a dead socket (it reads as
  "no data" and burns the namespace verdict).
- **Guest-open vs gated namespaces**: the client's namespace config
  (`authenticated:!1` flags) maps the surface — feeds marked guest-open stream to
  anonymous sockets while `/player-*` style namespaces return CONNECT_ERROR
  (`er_spectator_not_allowed`-shaped) or silence. Client-asserted auth objects
  (`{"x-public-id": <id>}`) are ignored on guest connections when the server derives
  identity from the session — a leaked PUBLIC id does not open gated namespaces.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
