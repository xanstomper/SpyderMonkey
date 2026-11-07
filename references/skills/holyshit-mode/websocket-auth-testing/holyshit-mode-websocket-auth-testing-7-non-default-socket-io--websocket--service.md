# 7. Non-default socket.io parsers: the msgpack silent-drop — websocket / service

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-7-non-default-socket-io.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **service** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

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

## Probe adjustment (websocket × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
