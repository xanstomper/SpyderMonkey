# engine.io v3 (EIO=3): capture discipline + custom-parser protocol replication — mobile / service

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-engine-io-v3-eio-3-capture-disci.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **mobile** · auth **service** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the client is another principal — storage/permission surface, own device only
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

**Capture first:**

1. **Hook `window.WebSocket` via `page.evaluateOnNewDocument`** — record `ws.url()`, wrap `send()` and the `message` listener. Sockets often open only on specific pages (chat/game), only after long dwells, and intermittently — retry navigations before concluding the lane is closed.
2. **Answer engine.io `'2'` pings with `'3'`** or the session dies in ~25s. A raw `new WebSocket()` without the app's query params closes 1006 even with valid cookies.
3. **Engine.io-over-WS needs no sid** — a websocket-only connect (no polling first) is valid when the URL carries the app's auth params.

**Decode the wire format from the client, not from captures:**

4. **Find the socket.io custom `parser` (Encoder/Decoder classes) in the SDK bundle and read its encode/decode** — captures alone won't reveal the frame layout. Typical layout: `[1B type (+128 when an ackId follows)][4B BE ackId][1B nsLen][namespace][1B evLen][event][protobuf payload]`; responses envelope as protobuf `ResultObj{code, msg, data}` (fields 1/2/3).
5. **Control packets go through the custom parser too** — namespace CONNECT is a BINARY frame carrying the namespace string, NOT socket.io text `'40/nsp'` (text `'40'` gets a default-ns ack; a text namespaced connect is silently dropped). **MIRROR THE APP'S PACKET TYPE**: capture the app's own outgoing CONNECT frames via CDP `Network.webSocketFrameSent` and use the EXACT type it sends (on bc.game the app sends **type 4** for all namespace connects; a hand-built **type-0** CONNECT yields a silent no-ack). The header carries `+128` when an ackId follows; the ackId is optional for the connect. Connect-acks arrive as binary frames the client's own decoder consumes silently — drive the sequence on timers, never wait for a text ack.

**Replicate the handshake when the client signs its connection:**

6. **Trace every socket-URL query param to its source** (`grep` for `this.opts.query =` in the SDK). Common chain: `t1(UA)` → GET `https://<socket-host>/test/?p=<t1sig>` → the raw response text is one param (`t`) and `t2(response, UA)` produces the other (`p`). Ticket endpoints like this often answer 200 to anyone presenting a valid signed transform, no user auth — itself a finding.
7. **Execute the target's own signing module instead of reversing it** — WASM/Rust transforms embedded as base64 data-URIs run in the page: `await import()` the chunk and call the exports. Module default exports may be PROMISES resolving to the function table — `await mod.default` before destructuring or you pass a promise into a signature slot.
8. **Copy the whole URI resolution, not just the host** — the SDK config can carry `socket` (prod) + `test` (dev) URIs, race them, and default the env to `development`; the app may also hit a different socket host than the main site's.

**Interpret results:**

9. **Interpreting acks: connect-accept vs data gate are DIFFERENT layers, and the packet type decides which you're seeing.** A binary type-4 namespace CONNECT (the app's own type) is ACKED by a healthy socket server for EVERY namespace a client can dial — on bc.game an anonymous socket (attacker-chosen fingerprint, no session) got connect-ACKs on all of `/bet/log`, `/user`, and `/game-support`. That only proves namespace-connect is not gated; it does NOT prove data flows. The real gate is the EVENT/DATA layer: sending `get-all-bet`/`join-all-bet`/`history`/`detail` on `/bet/log` from that same anonymous socket returns only engine.io ping-acks — zero data. AVOID THE FALSE-GATE TRAP: a silent no-ack on a hand-built connect is usually YOUR packet type or framing being wrong (type 0 vs the app's type 4), not a server-side `/merchants` gate — verify the app's own type before concluding that a namespace is authenticated-server-side. Register the event-layer gate as a decisive negative (disproving an IDOR at the protocol layer is a finding), but never cite a mis-framed connect as proof of server auth.
10. **The edge gate closes with volume — and it is PER-LANE, with a long cooldown**:
    after a heavy probing burst the WS-upgrade lane stops opening entirely (0 opens across
    retries with a correct recipe) — edge anomaly response, not a code bug. The HTTP
    fetch lane on the SAME origin keeps answering (t1 ticket mints 200, page fetches
    fine) while the socket lane stays closed for many minutes; a 10s wait is NOT enough,
    budget minutes and pace/rotate, and never conclude the host is down from socket
    lane alone. A raw `new WebSocket()` from a DIFFERENT IP that never had CF clearance
    fails non-101 ("Just a moment") — the VM's cleared page context is the only socket
    lane; don't rewrite working client code.

## Probe adjustment (mobile × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
