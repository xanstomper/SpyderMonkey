# Economy map (the "free money" surface) — grpc / low-priv

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-economy-map-the-free.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- context: **grpc** · auth **low-priv** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Faucet: `POST /public/cx-bucks/claim`; config `GET /public/cx-bucks/rewards`. Response reason enum `ok|claimed|on_cooldown|disabled|requirements_not_met`; gates `min_account_age_days`, `min_global_level`; ledger grant kinds include `website_claim`, `chat_reward`, `trivia_reward`. REQUIRES Kick session — untested (blocked).
- Gambling (exact values from cached `/public/gambling/config`): wagers 100–500 cents; plinko/slots/mines(≤15)/crash(cap 1000x, min auto-cashout 1.01x) all enabled. Slots payout table client-visible: murat 4.24x, amray 10.6x, nickwhite 35x, ice 95.4x, don 286.1x, nate 1165.6x.
- Store chain: `cxBucksStore.checkout` → `my-orders` → **`launch`** (fires the purchased effect at the live event). `event-availability?product_kind=` pre-check; `validate-coupon` endpoint exists.
- Deliveries enum: `missile|abz_missile|nuke|horde|tear_gas|care_package`. Nuke: target radius 300m, blast 100m, 20 dmg, 60s flight; target REQUIRED for nuke/missile/tear_gas; availability gated by `emp_active` + clearance + target_area.

## Probe adjustment (grpc × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
