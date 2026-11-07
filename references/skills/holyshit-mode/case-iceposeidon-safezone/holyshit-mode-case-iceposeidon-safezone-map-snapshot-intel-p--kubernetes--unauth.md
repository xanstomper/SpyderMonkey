# Map-snapshot intel (public, unauth)- `GET /event/map-snapshot` → 11 frames. JSON frames: event state, map_objects, contestants roster (inventory/effects/HP), game_items (211 dropped items/gravestones w/ exact lat/lng + contents), tracked_devices (live GPS + heading of tracked participants, e.g. "nate" 30.2489,-97.7236 acc 4.9m). — kubernetes / unauth

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-map-snapshot-intel-p.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **kubernetes** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- 45 `claimable` chests, exact coords (~30.2509,-97.7291 Austin TX), `is_secret:true`, `claim_radius_m:10` — full chest GPS dumped publicly.
- Binary frames (types 1/2/4/7/8): **PROTOCOL FULLY CRACKED (2026-10-21)** — see `references/iceposeidon-binary-map-protocol.md`. Kind 1 = contestant GPS fixes (slot, lat/lng i16 deltas from i32 base /1e5, accuracy, age); kinds 2/7/8 = health/zombies/projectiles. Decoded real positions (slots 21/27/67 @ ~30.2548,-97.7301).

## Probe adjustment (kubernetes × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
