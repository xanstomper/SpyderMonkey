# 5.2 WebSocket auth (score 85 — full class in `websocket-auth-testing.md`)

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
