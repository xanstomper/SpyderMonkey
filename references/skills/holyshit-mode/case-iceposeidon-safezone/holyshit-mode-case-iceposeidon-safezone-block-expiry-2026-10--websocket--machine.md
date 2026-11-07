# Block expiry (2026-10-21 ~01:25Z): 403 Blocked LIFTED, full unauth re-sweep — websocket / machine

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-block-expiry-2026-10.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **websocket** · auth **machine** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Per-IP origin block expired on its own (~24h retry-after honored). Re-sweep immediately when retry-after lapses — same routes that 403'd now return 200/400/401.
- **NEW unauth finds (ledger probes #4–5):**
  - `GET /public/cx-bucks-store/products` (unauth) → full catalog w/ UUIDs: nuke $10,000 (1,000,000¢), missile/abz $1,500, horde $4,000, tear-gas $750, care-package $500, crate $1,000. `store_access:"logged_in_only"` field is just a flag; the products list itself is public.
  - `GET /public/cx-bucks-store/event-availability?product_kind=nuke` (unauth) → **targeting config leak**: blast radius, grace distance, AND safe-zone center coords + radius (where nukes are banned). Same shape for missile/abz/tear_gas (tear_gas adds `contestant_clearance_m`).
  - `GET /public/stock-market/stocks` + `/stocks/:externalId/trades` + `/candles` (unauth) → complete viewer trade feed with user_ids, share counts, fees, price_before. Cross-join user_ids against `/public/leaderboards?category=X` (15 categories: richest, gambling_net, event_damage_dealt/kills/items_stolen/zombie_leech…). **Front-run vector**: an authed viewer polling the trades feed faster than the UI can front-run the AMM; the feed itself is the leak.
  - `GET /public/polls/winner` (unauth) → live vote %s + contestant UUIDs (`my_vote:null` — write is authed). `GET /public/store/config` → TTS/store limits unauth.
- **Zod validates BEFORE auth on api.* routes**: bad bodies on authed routes return 400 field-validation errors (not 401) — free schema oracle without credentials, but never reaches state. `mines/start` limits (mine_count 3–15) recovered this way. Auth enforced after validation on checkout/launch/claim/buy/validate-coupon — all 401. **No unauth write path exists anywhere.**
- Robot control backend: 502 upstream (service down, not a block). Traffic-cams: `traffic-cams.iceposeidon.com/cameras/austin/<ID>/timelapse.mp4` unauth 200 real MP4s, IDs enumerable via Austin open-data `b4k4-adkb.json` (low impact, banked score 60).

## Probe adjustment (websocket × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
