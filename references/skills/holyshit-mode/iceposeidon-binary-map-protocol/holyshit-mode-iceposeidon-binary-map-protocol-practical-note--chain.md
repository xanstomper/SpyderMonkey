# Practical notes — chain composition

- source canon: `holyshit-mode/i***REDACTED***-binary-map-protocol.md`
- base technique: `holyshit-mode-i***REDACTED***-binary-map-protocol-practical-note.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Quiet event = one full snapshot per kind at connect, then heartbeat + JSON patches only. Don't conclude "no fixes stream" from a short idle window.
- Text frames (op=1) JSON types: heartbeat, event, map_objects, map_objects_patch, contestants, game_items, tracked_devices.
- Handshake (stdlib, no deps): GET /public-map-ws with Origin + Sec-WebSocket-Key/Version; read frames manually (2-byte hdr; op=1 text, op=2 binary; extended lengths 126/127).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
