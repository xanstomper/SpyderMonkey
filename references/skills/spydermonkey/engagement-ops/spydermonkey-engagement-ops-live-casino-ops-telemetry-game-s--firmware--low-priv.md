# Live casino-ops telemetry: game-stat endpoints expose RTP windows without auth — firmware / low-priv

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-live-casino-ops-telemetry-game-s.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **firmware** · auth **low-priv** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

After the history lane, probe the game-stat family with the CLIENT'S EXACT VERB AND BODY —
one GET answered 500 `Service error` while the app's own `POST {gameUrl:"crash"}` returned
200 with `liveRtp_5m / liveRtp_1h / liveRtp_24h`, `onlinePlayers`, favorite/like counts.
GET vs POST is the whole difference; mirror the bundle's call (find it via `STAT_URL`-style
constants in third-party engines or `postJson` in the app) before declaring an endpoint
broken. Live RTP windows running BELOW the advertised config RTP (0.96) — e.g. 1h at
~0.80 — is a report-and-fix item on its own: the operator's own unauthenticated telemetry
outs the shortfall, and it compounds the dead-verifier finding (players cannot audit).
Register as INFO_DISCLOSURE with the returned values in the proof.

**Sweep the whole catalog, not one game.** The same endpoint answers for EVERY game in the
catalog — enumerate the game keys from the config chunk (the `key:"crash",ns:"/g/cm/98",
rtp:.98` entries) and POST one per game (300–400ms pacing; null `liveRtp_*` windows mean
the game doesn't publish them, not a failure). Then sort by `liveRtp_24h` and work BOTH
tails: values > 1.0 mean the house is paying out more than it takes (player-favorable
EV — a money-pump/arbitrage class finding, CRITICAL if sustained well above 1.0), and
values far below the game's advertised `rtp` field (config chunk) are player-hostile
outliers (e.g. a 5% RTP game with hundreds of favorites). The deviation from the game's
OWN advertised rtp is the finding, not the raw number.

Evidence discipline for a >1.0 outlier (two readings, state both): (a) genuine overpay —
min-bet grind yields positive EV, bounded only by max-bet/session caps; or (b) RTP
accounting bug — free-bet winnings (games carry `freeBet:!0`) counted in the numerator
without their wagers in the denominator, which inflates the published RTP and is itself
false telemetry shown to every visitor. Stability checks: values identical across two
samples 30s apart are a CACHED rolling-24h aggregate — consistent with real data, not a
fake; cross-check `onlinePlayers`/`favoriteNum` moving while RTP holds. A 24h window is a
large sample, so a lone >1.0 is stronger when 5+ sibling games cluster near normal
(0.82–1.09) — the outlier stands out against the cluster.

Trap: near-identical display names are SEPARATE catalog entries with SEPARATE RTP — e.g.
`dice`, `hash-dice`, `classic-dice` are three different games (one bled at 1.2959, the
others clustered ~0.96). Sweep with the exact `key:` values from the config chunk, never
a fuzzy display-name guess, or you will statically analyze the wrong game's math (and
its client formula may be perfectly fair while the sibling game's live telemetry is not).

Single-player games do NOT appear in the public multi/history feed: `POST
/game/bet/multi/history {gameUrl:<single-player>}` returns an EMPTY list (page 0 / total
0), not an error, and their own history endpoints (`recent-bet` etc.) sit behind the
auth gate — so per-round seeds/round data for single-player games are only reachable with
a session, and a pre-round seed-predictiveness test stays behind that same gate. Also:
the history API REFUSES small pageSize (e.g. 2 → custom 4001 `page_size_incorrect`) —
always mirror the client's own pageSize (50/100).

## Probe adjustment (firmware × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
