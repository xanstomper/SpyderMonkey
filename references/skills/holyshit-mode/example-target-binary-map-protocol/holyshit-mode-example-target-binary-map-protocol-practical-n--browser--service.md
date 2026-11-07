# Practical notes — browser / service

- source canon: `holyshit-mode/example-target-binary-map-protocol.md`
- base technique: `holyshit-mode-example-target-binary-map-protocol-practical-n.md`
- bindings: **WSTG-CLNT-05** · **CWE-345** · **ATT&CK T1557**
- context: **browser** · auth **service** · chain role **pivot**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- Quiet event = one full snapshot per kind at connect, then heartbeat + JSON patches only. Don't conclude "no fixes stream" from a short idle window.
- Text frames (op=1) JSON types: heartbeat, event, map_objects, map_objects_patch, contestants, game_items, tracked_devices.
- Handshake (stdlib, no deps): GET /public-map-ws with Origin + Sec-WebSocket-Key/Version; read frames manually (2-byte hdr; op=1 text, op=2 binary; extended lengths 126/127).

## Probe adjustment (browser × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
