# Live map websocket (unauth, verified 2026-10-21)

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

### CONFIRMED HOLYSHIT #1 — unauth realtime GPS surveillance (score 90)
Streaming kind-1 fixes at ~300ms + `tracked_devices` JSON = meter-precision live tracking of real people with zero credentials. Verified: Nate tracked-device at **3.8m accuracy + live heading (~146°, walking S)** updating ~1/s; contestant slots 21/27/67 tracked continuously; tracker also correlates staff↔contestant proximity (slot 27 was ~20m from Nate's device). Invisible-status contestants still appear in binary fixes (invisibility hides on map render, not in stream).

### CONFIRMED HOLYSHIT #2 — hidden-layer tactical intel via plain REST (score 85)
`GET /event/contestants` (unauth) exposes what the public map does NOT render: exact HP/maxHP of every remaining player, full inventories (EMPs, invisibility cloaks, machetes, guardian angels), active effects (mirror_forcefield, shield, invisible), live-on-Kick flag, last_damaged_at timestamps. Cause: `stats_visible: true` in event config broadcasts the hidden layer. `/event/config` dumps full game rules (nuke 300m target/100m blast/20dmg/60s, c4, poison, trade rules, zombie counts).

### Verified negatives (don't re-test)
- WS ignores ALL client→server messages (`ping`, `subscribe`, forged `viewer_action` nuke) — server streams its cycle regardless. No injection without auth.
- REST on event-public is read-only (uWebSockets/20; POST/PUT/DELETE → 404). Param fuzzing (`?include_hidden/full/expand=all`) changes nothing.
- No additional WS endpoints (`/ws`, `/event-ws`, `/actions-ws`, `/viewer-ws` all 404); no other open sibling hosts (event./safezone./actions. = NXDOMAIN; ws./data.cx-live./files. = bare 404s).

- `wss://event-public.iceposeidon.com/public-map-ws` — handshake needs only `Origin: https://iceposeidon.com` + `Sec-WebSocket-Version: 13`. No token, no cookie.
- Text JSON types: `heartbeat` (server_time), `event` (upstream/map state: damage active, blackout `{until,source:"emp"}`), `map_objects`/`map_objects_patch` (upserts), `contestants` (roster: name, kick_slug, avatar_url, eliminated_at, live_seconds, inventory), `game_items`, `tracked_devices` (live GPS of tracked participants).
- Binary frames share a 36-byte header: `[0]kind u8, [1]version=1, [2]flags u16 (1=full, 2|=clear, 4=sparse), [4]generation u32, [8]sequence u32, [12]eventRevision f64, [20]sampledAt f64 ms, [28]partIndex u16, [30]partCount u16, [32]recordCount u16, [34]reserved`.
- Key decoder constants from `cx-client` (minified names vary by build): `bt=36` header, `$r=1e7` coord grid, `Re=1e5` map fix scale, `Yi=[disabled,paused,inside,outside,unavailable,eliminated]` health enum.
- On a quiet event you get one full snapshot per kind at connect then only heartbeat+patches. During active play, kind-1 fixes stream at ~300ms — replay the decoder for a live tracker.
- **Raw-socket WS client pattern (no pip installs, PEP 668-safe)**: stdlib `socket.create_connection((host,443))` → `ssl.wrap_socket(server_hostname=...)` → manual handshake with random Sec-WebSocket-Key → parse frames: 2-byte hdr, `op=h[0]&0xf`, `ln=h[1]&0x7f`, ext len u16/u64 when 126/127. Text frames op=1 JSON, binary op=2. Works for any unauth WS recon without deps.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
