# 5.2 WebSocket auth (score 85 — full class in `websocket-auth-testing.md`) — websocket / hardened

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- base technique: `3am-shinjitsu-arsenal-05-client-side-5-2-websocket-auth-scor.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **websocket** · auth **hardened** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- 101 Switching Protocols is a CDN passthrough, NOT auth. Naive curl = false negative.
- DECISIVE: real frame exchange (python socket+ssl): token-in-first-frame / query-param /
  cookie / signed-URL patterns; CLOSE 1008 on first frame = gate works (negative).
- sid-reuse hijack: second WS against a live session's sid → 101 + answered pings = sid is a
  bearer credential; Origin allowlist is client-asserted (fakeable from non-browser clients).
- socket.io: BOTH EIO=3 and EIO=4 (prod client often speaks the older one); unknown namespace
  acks `40` then `44 "Invalid namespace"` 1-2s later (listen ≥2s); RPC-over-HTTP
  (`POST /stream<ns>/rpc/<method>`): `unknown rpc` vs `Invalid parameters` (live) vs
  `Cannot POST` (dead) = full method map unauth. Synthetic sockets: websocket transport ONLY
  (CDN node affinity breaks polling).
- engine.io path + grpc-gateway fronting: `400 {"code":3,"message":"Bad request"}` on
  handshake = gateway, not dead host — route through a real socket.io client.
- msgpack/CFR frames: decode the protocol from the client codec, test frame injection
  server-side validation (rainbet class).
- Unauth-ns-connect proof (raw polling, box-reachable host): handshake GET
  `?EIO=4&transport=polling` with NO auth payload → sid issued? → POST body `40` (ns
  connect) → ack `40{"sid":...}` PLUS an UNPROMPTED server broadcast (`42["game-state",...]`
  class) = the auth seam CONFIRMED — the server streams state to credential-less sessions.
  Polling needs POST, so it runs from a host the box reaches directly (exempt path class,
  edge-gate-recon), never through GET-only relays; CDN-affinity hosts stay websocket-only.
- Event-vocabulary mining before any emit: grep every chunk for `\.emit\(\s*"([a-z_.-]+)"`,
  `\.on\(\s*"([a-z_.-]+)"`, and bare `"(subscribe|join|joinChannel|leave|raffle[a-z_]*|chat[a-z_.]*|alert[a-z_]*)"`
  literals — the vocab feeds the event probes. Emit at most ONE read-shaped event per
  candidate, observe ONE batch, stop — no harvesting, no bulk event capture.

## Probe adjustment (websocket × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
