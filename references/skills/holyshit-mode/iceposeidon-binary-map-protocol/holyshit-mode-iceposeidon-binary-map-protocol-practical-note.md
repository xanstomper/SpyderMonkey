# Practical notes

- source canon: `holyshit-mode/iceposeidon-binary-map-protocol.md`
- bindings: **WSTG-CLNT-05** · **CWE-345** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

- Quiet event = one full snapshot per kind at connect, then heartbeat + JSON patches only. Don't conclude "no fixes stream" from a short idle window.
- Text frames (op=1) JSON types: heartbeat, event, map_objects, map_objects_patch, contestants, game_items, tracked_devices.
- Handshake (stdlib, no deps): GET /public-map-ws with Origin + Sec-WebSocket-Key/Version; read frames manually (2-byte hdr; op=1 text, op=2 binary; extended lengths 126/127).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
