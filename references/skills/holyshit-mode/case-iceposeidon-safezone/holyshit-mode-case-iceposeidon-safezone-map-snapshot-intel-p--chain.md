# Map-snapshot intel (public, unauth)- `GET /event/map-snapshot` → 11 frames. JSON frames: event state, map_objects, contestants roster (inventory/effects/HP), game_items (211 dropped items/gravestones w/ exact lat/lng + contents), tracked_devices (live GPS + heading of tracked participants, e.g. "nate" 30.2489,-97.7236 acc 4.9m). — chain composition

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-map-snapshot-intel-p.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- 45 `claimable` chests, exact coords (~30.2509,-97.7291 Austin TX), `is_secret:true`, `claim_radius_m:10` — full chest GPS dumped publicly.
- Binary frames (types 1/2/4/7/8): **PROTOCOL FULLY CRACKED (2026-10-21)** — see `references/iceposeidon-binary-map-protocol.md`. Kind 1 = contestant GPS fixes (slot, lat/lng i16 deltas from i32 base /1e5, accuracy, age); kinds 2/7/8 = health/zombies/projectiles. Decoded real positions (slots 21/27/67 @ ~30.2548,-97.7301).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
