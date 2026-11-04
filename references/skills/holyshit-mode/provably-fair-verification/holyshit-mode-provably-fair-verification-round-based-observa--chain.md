# Round-based observables + the idle-game blocker — chain composition

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-round-based-observa.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
