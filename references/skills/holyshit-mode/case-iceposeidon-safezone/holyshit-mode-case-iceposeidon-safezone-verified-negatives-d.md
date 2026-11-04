# Verified negatives (don't re-test)

- source canon: `holyshit-mode/case-i***REDACTED***-s***REDACTED***.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

- WS ignores ALL client→server messages (`ping`, `subscribe`, forged `viewer_action` nuke) — server streams its cycle regardless. No injection without auth.
- REST on event-public is read-only (uWebSockets/20; POST/PUT/DELETE → 404). Param fuzzing (`?include_hidden/full/expand=all`) changes nothing.
- No additional WS endpoints (`/ws`, `/event-ws`, `/actions-ws`, `/viewer-ws` all 404); no other open sibling hosts (event./s***REDACTED***./actions. = NXDOMAIN; ws./data.cx-live./files. = bare 404s).

- `wss://event-public.i***REDACTED***.com/public-map-ws` — handshake needs only `Origin: https://i***REDACTED***.com` + `Sec-WebSocket-Version: 13`. No token, no cookie.
- Text JSON types: `heartbeat` (server_time), `event` (upstream/map state: damage active, blackout `{until,source:"emp"}`), `map_objects`/`map_objects_patch` (upserts), `contestants` (roster: name, kick_slug, avatar_url, eliminated_at, live_seconds, inventory), `game_items`, `tracked_devices` (live GPS of tracked participants).
- Binary frames share a 36-byte header: `[0]kind u8, [1]version=1, [2]flags u16 (1=full, 2|=clear, 4=sparse), [4]generation u32, [8]sequence u32, [12]eventRevision f64, [20]sampledAt f64 ms, [28]partIndex u16, [30]partCount u16, [32]recordCount u16, [34]reserved`.
- Key decoder constants from `cx-client` (minified names vary by build): `bt=36` header, `$r=1e7` coord grid, `Re=1e5` map fix scale, `Yi=[disabled,paused,inside,outside,unavailable,eliminated]` health enum.
- On a quiet event you get one full snapshot per kind at connect then only heartbeat+patches. During active play, kind-1 fixes stream at ~300ms — replay the decoder for a live tracker.
- **Raw-socket WS client pattern (no pip installs, PEP 668-safe)**: stdlib `socket.create_connection((host,443))` → `ssl.wrap_socket(server_hostname=...)` → manual handshake with random Sec-WebSocket-Key → parse frames: 2-byte hdr, `op=h[0]&0xf`, `ln=h[1]&0x7f`, ext len u16/u64 when 126/127. Text frames op=1 JSON, binary op=2. Works for any unauth WS recon without deps.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
