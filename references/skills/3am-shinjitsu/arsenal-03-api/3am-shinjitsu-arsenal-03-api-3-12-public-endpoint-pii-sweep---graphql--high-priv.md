# 3.12 Public-endpoint PII sweep (score 80 — easy HIGH wins live here) — graphql / high-priv

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-12-public-endpoint-pii-sweep-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **graphql** · auth **high-priv** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- SET: `/api/leaderboard/*`, `/api/health`, `/api/models/status`, `/api/catalog`,
  `/api/version`, `/api/ping`, `/profile/{username}/public`-shaped, bet feeds (`/ws/user/bets/live`).
- CONFIRMED: cross-user PII, internal UUIDs + registration-ms + authRole alongside public
  fields, per-user FINANCIALS (deposits/withdrawals/per-game profit) + username-enumeration
  oracle (200/404/422).
- Boolean payload flags lie until read at the CONSUMER — semantics live at the use site.

## Probe adjustment (graphql × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
