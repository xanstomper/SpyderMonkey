# Block expiry (2026-10-21 ~01:25Z): 403 Blocked LIFTED, full unauth re-sweep — chain composition

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-block-expiry-2026-10.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Per-IP origin block expired on its own (~24h retry-after honored). Re-sweep immediately when retry-after lapses — same routes that 403'd now return 200/400/401.
- **NEW unauth finds (ledger probes #4–5):**
  - `GET /public/cx-bucks-store/products` (unauth) → full catalog w/ UUIDs: nuke $10,000 (1,000,000¢), missile/abz $1,500, horde $4,000, tear-gas $750, care-package $500, crate $1,000. `store_access:"logged_in_only"` field is just a flag; the products list itself is public.
  - `GET /public/cx-bucks-store/event-availability?product_kind=nuke` (unauth) → **targeting config leak**: blast radius, grace distance, AND safe-zone center coords + radius (where nukes are banned). Same shape for missile/abz/tear_gas (tear_gas adds `contestant_clearance_m`).
  - `GET /public/stock-market/stocks` + `/stocks/:externalId/trades` + `/candles` (unauth) → complete viewer trade feed with user_ids, share counts, fees, price_before. Cross-join user_ids against `/public/leaderboards?category=X` (15 categories: richest, gambling_net, event_damage_dealt/kills/items_stolen/zombie_leech…). **Front-run vector**: an authed viewer polling the trades feed faster than the UI can front-run the AMM; the feed itself is the leak.
  - `GET /public/polls/winner` (unauth) → live vote %s + contestant UUIDs (`my_vote:null` — write is authed). `GET /public/store/config` → TTS/store limits unauth.
- **Zod validates BEFORE auth on api.* routes**: bad bodies on authed routes return 400 field-validation errors (not 401) — free schema oracle without credentials, but never reaches state. `mines/start` limits (mine_count 3–15) recovered this way. Auth enforced after validation on checkout/launch/claim/buy/validate-coupon — all 401. **No unauth write path exists anywhere.**
- Robot control backend: 502 upstream (service down, not a block). Traffic-cams: `traffic-cams.iceposeidon.com/cameras/austin/<ID>/timelapse.mp4` unauth 200 real MP4s, IDs enumerable via Austin open-data `b4k4-adkb.json` (low impact, banked score 60).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
