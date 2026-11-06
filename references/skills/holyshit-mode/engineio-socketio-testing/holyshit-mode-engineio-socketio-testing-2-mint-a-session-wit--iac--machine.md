# 2. Mint a session WITHOUT polling (bypass CDN affinity) — iac / machine

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-2-mint-a-session-wit.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iac** · auth **machine** · chain role **pivot**

## Context

- platform: template/state files are the infrastructure inventory — read-only crown of the exposure
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- CDN-node affinity (Fastly/Varnish) kills sequential polling from python: handshake 200 + sid, then every follow-up poll = `{"code":1,"message":"Session ID unknown"}` — requests land on different edge nodes and the in-memory engine session is gone. Cookie-pinning (`io=<sid>`) does NOT reliably fix it.
- Use the WEBSOCKET-FIRST handshake: `GET /socket.io/?EIO=3&transport=websocket` with NO `sid` — many servers mint the session over the websocket itself (first frame `0{"sid":...}`), on both EIO=3 and EIO=4.
- Always send browser headers INCLUDING `Origin: <target origin>` — the handshake origin-check is enforced at the transport.
- Short-TTL anon socket tokens are often mintable from a PUBLIC metadata endpoint (duel-family: `GET /api/v2/metadata?uuid=000000` returns `socket_token` + rooms + feature-flag table in ONE unauth response). Mint INSIDE the connect script — the JWT can expire in 30s. Token placement = read it off the page's real handshake; usually the QUERY (`?uid=guest&token=<jwt>&EIO=4&transport=websocket`), not the connect payload. A connect that 101s then immediately `41`s = wrong placement, not an auth wall.
- Placement VARIES by server: socket.io v4 commonly takes the token in the CONNECT frame payload (`40{"token":"<jwt>"}`) — a bare `40` that 101s then answers `44{"message":"Could not establish connection"}` means namespace auth is MISSING, not an auth wall; re-handshake and resend with the token in the frame. Tokens often mint UNAUTH from a dedicated endpoint (`POST /auth/token?scope=X`) — see the scope-abuse pattern in SKILL.md.
- Definitive handshake capture when the bundle-derived URL 400s: `performance.getEntriesByType('resource')` does NOT list WebSocket URLs. Install a persistent hook via CDP — `Page.addScriptToEvaluateOnNewDocument` wrapping `window.WebSocket` to push URLs into a `window.__wsUrls` array — then navigate the harness browser across game pages and read the array. One SPA connection serves all namespaces (route changes add namespaces, not connections), so collect across pages before concluding the map.
- Reply `3` (pong) to every `2` (ping) DURING captures: pingInterval 25–45s + pingTimeout ~20s means an un-pong'd capture dies silently mid-listen (~60–90s in) and reads as an event lull. Silent capture death = check the pong path first.

## Probe adjustment (iac × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
