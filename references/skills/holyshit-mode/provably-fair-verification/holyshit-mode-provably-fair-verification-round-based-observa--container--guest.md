# Round-based observables + the idle-game blocker — container / guest

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-round-based-observa.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **container** · auth **guest** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- Round-history/state feeds are often UNAUTH even when betting is session-gated:
  `/ws/games/<game>/history` (round id + ticket + participants), `/ws/games/<game>/state`
  (live round incl. other players' open bets), `/ws/games/<game>/seeds` (period seeds).
  These are the observable source for the derivation test — no session needed.
- **Seed-period model:** daily/global seed periods with `startRound` boundaries (roulette
  pattern). Verify every closed period `sha256(serverSeed)==serverSeedHash`, then run the
  direction test across periods.
- **Idle-game blocker:** rounds with `participants==0` never draw a ticket — an idle game
  yields zero observable outcomes and blocks the derivation test no matter the pagination.
  Check `participants>0` in the captured window BEFORE planning the test; if the game is
  idle, wait for played rounds or state the test is blocked on observables.
- **Live-period display bug (never score as a leak):** the ACTIVE period's seed record often
  carries the commitment hash in the `serverSeed` field (`serverSeed == serverSeedHash`).
  Hash ≠ preimage — nothing is derivable. Real impact: player-side verification of the
  active period fails → false-rigging dispute fodder. Report as a verification-flow bug:
  the seed field must be null until the period closes.

## Probe adjustment (container × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
