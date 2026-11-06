# 11. msgpack-parser targets (frames look "auth-gated" when the gate is the wire format) — chain composition

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-11-msgpack-parser-ta.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Some stacks run socket.io with the **msgpack parser** — EVERY text frame (`40`, `40{}`,
`42[...]`) is silently dropped: no ack, no error, no data. Naive testing concludes
"namespace auth-gated" when the gate is just the encoding. Discriminate before scoring.

- **Capture the REAL client before hand-rolling anything.** CDP: `Network.enable` BEFORE
  `Page.navigate` on a fresh tab, then collect `webSocketFrameSent/Received` — CDP delivers
  frame bytes base64-encoded; decode with `msgpack.unpackb`. The connect frame is
  `{type:0, data:{}, nsp:"/ns"}` — data is an EMPTY MAP, not nil (a nil data field gets
  dropped). Events = `{type:2, data:[name,args], nsp}`. Server acks carry a `pid` msgpack
  ext. performance.getEntries does not list sockets — Network events are the only source.
- **Best vantage = frame injection onto the SPA's own trusted connection.** Via
  `Page.addScriptToEvaluateOnNewDocument`, wrap `window.WebSocket` to record `send` and
  incoming messages per connection; then send hand-rolled msgpack bytes through the SPA's
  live socket. Replica sockets with byte-identical frames and the same cookies get CLOSED
  ~1-2s after the first packet (a connection-level gate the replica fails — registration or
  transport fingerprint), but frames injected on the trusted connection are processed
  normally. Injection sidesteps the connection gate entirely.
- **Protocol violations kill the connection SILENTLY.** An EVENT on a namespace never
  CONNECTed, or any malformed packet = the socket just stops (no error frame). After any
  violation RELOAD the page and re-inject; never re-probe on a dead socket — it reads as
  "no data" and burns the namespace verdict.
- **Guest-open vs gated namespaces: read the client's namespace config map
  (`authenticated:!1/!0` per namespace), then VERIFY each.** Config says guest-open but the
  server still enforces: expect CONNECT_ERROR (`er_spectator_not_allowed`-style) on gated
  namespaces and silent drops on chat joins. Both shapes = the gate, log which.
- **Hex-capture hygiene: pad every byte** (`x.toString(16).padStart(2,'0')`) — bare
  `toString(16)` drops leading zeros and silently corrupts msgpack bytes (map16 lengths,
  0x00 bytes) so hand-decoding garbles. Decode captured frames with the msgpack library,
  never by eyeballing hex.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
