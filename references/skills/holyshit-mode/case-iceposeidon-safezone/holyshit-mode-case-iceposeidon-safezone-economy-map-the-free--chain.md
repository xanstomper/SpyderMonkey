# Economy map (the "free money" surface) — chain composition

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-economy-map-the-free.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Faucet: `POST /public/cx-bucks/claim`; config `GET /public/cx-bucks/rewards`. Response reason enum `ok|claimed|on_cooldown|disabled|requirements_not_met`; gates `min_account_age_days`, `min_global_level`; ledger grant kinds include `website_claim`, `chat_reward`, `trivia_reward`. REQUIRES Kick session — untested (blocked).
- Gambling (exact values from cached `/public/gambling/config`): wagers 100–500 cents; plinko/slots/mines(≤15)/crash(cap 1000x, min auto-cashout 1.01x) all enabled. Slots payout table client-visible: murat 4.24x, amray 10.6x, nickwhite 35x, ice 95.4x, don 286.1x, nate 1165.6x.
- Store chain: `cxBucksStore.checkout` → `my-orders` → **`launch`** (fires the purchased effect at the live event). `event-availability?product_kind=` pre-check; `validate-coupon` endpoint exists.
- Deliveries enum: `missile|abz_missile|nuke|horde|tear_gas|care_package`. Nuke: target radius 300m, blast 100m, 20 dmg, 60s flight; target REQUIRED for nuke/missile/tear_gas; availability gated by `emp_active` + clearance + target_area.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
