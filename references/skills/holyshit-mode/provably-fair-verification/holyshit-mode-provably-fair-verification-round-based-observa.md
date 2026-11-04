# Round-based observables + the idle-game blocker

- source canon: `holyshit-mode/provably-fair-verification.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
