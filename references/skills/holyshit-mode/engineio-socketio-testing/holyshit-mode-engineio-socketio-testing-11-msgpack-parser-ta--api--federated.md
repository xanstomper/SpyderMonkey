# 11. msgpack-parser targets (frames look "auth-gated" when the gate is the wire format) — api / federated

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-11-msgpack-parser-ta.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

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

## Probe adjustment (api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
