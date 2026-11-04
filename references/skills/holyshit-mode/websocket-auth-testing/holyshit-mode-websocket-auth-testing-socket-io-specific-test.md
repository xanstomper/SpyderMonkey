# Socket.io-Specific Testing (namespaces, transports, session tokens)

- source canon: `holyshit-mode/websocket-auth-testing.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

socket.io targets need tests the generic WS recipe above doesn't cover:

### 1. Namespace discovery — wait for the rejection frame

Unknown namespaces STILL ack `40` (connected) immediately; the server sends
`44<ns>,"Invalid namespace"` only after ~1-2 seconds. A recv window shorter than
that misreads EVERY namespace as live. Connect, then listen ≥2s per namespace and
classify: `40<ns>,` kept = real, `44` follows = rejected.

Then map the RPC layer — socket.io apps often route RPCs over HTTP as a SEPARATE
surface (`POST /stream<ns>/rpc/<method>` with body `{"type":"rpc","arg":...}`).
Existence oracle: unknown method → literal `unknown rpc`; live method, bad args →
`Invalid parameters`; dead namespace path → Express `Cannot POST`. Cross the two
axes for a full method×namespace map with zero credentials.

### 2. Protocol-version drift — test BOTH EIO versions

Servers frequently expose socket.io v2 (`EIO=3`) AND v4 (`EIO=4`) simultaneously,
and the production client often speaks the OLDER one. Synthetic testing against the
wrong protocol version tests a surface the real app doesn't use. Grab the production
URL from page traffic (`wss://host/socket.io/?EIO=3&transport=websocket&sid=...`)
and mirror its version.

### 3. Synthetic sockets: websocket transport only

Sequential HTTP polling from a script dies on CDN node affinity — each request lands
on a different backend and the in-memory session returns `"Session ID unknown"`.
One long-lived websocket connection is immune. And on EIO=3 the websocket-FIRST
handshake works with NO polling pre-step: `GET /socket.io/?EIO=3&transport=websocket`
(no sid) returns 101 and the server pushes `0{"sid":...}` as the first frame — own
session in one connection, no affinity problem. (Synthetic `io=<sid>` cookies do NOT
fix polling affinity — the cookie is not honored by the routing layer.)

### 4. Sid bearer-attach test

engine.io sessions authenticate by sid alone unless the app binds them server-side:
open a SECOND websocket against a LIVE session's sid (`?...&sid=<victim sid>`).
`101 Switching Protocols` + answered pings = the sid is a single-secret bearer
credential. The websocket Origin allowlist is client-asserted (header VALUE
comparison at handshake) — trivially faked from non-browser clients, so it does not
protect the session. A leaked sid (access logs, any reflection) on an AUTHED socket
= full event-stream takeover. Remediation to state: bind socket sessions to the HTTP
session cookie server-side (reject connections whose cookie doesn't match the
handshake session).

### 5. Unauth emit fencing

Gated namespaces usually kill anonymous emitters: send a `42<ns>,["event",...]`
frame unauth and watch for the server's `41` (namespace disconnect) — that IS the
fence working. Log it; don't retry the emit. Order matters: fire benign probes
(say/lastRain) BEFORE gate probes (join moderators) — the first gated emit kills
the namespace and everything after it reads as "no reply".

### 6. Capture: reassemble continuation frames, sanitize binaries

Large socket.io events fragment across websocket frames (continuations, opcode 0).
A recv loop that treats one frame per message splices JSON at ~4KB boundaries and
"Unterminated string" parse errors. Read one FULL message per recv: loop until the
FIN bit, merging opcode-0 payloads into the opcode-1 message. Pongs and other
binary frames arrive as 2-byte opcodes mid-stream — strip `\x00-\x1f` control
bytes from captured text before any JSON parse. A mis-reassembled capture will make
a 90KB `initialize` event parse as a 4KB stub — size-check messages before
trusting field counts.

### 7. Non-default socket.io parsers: the msgpack silent-drop

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
