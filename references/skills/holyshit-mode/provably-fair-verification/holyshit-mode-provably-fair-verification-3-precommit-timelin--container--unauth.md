# 3. Precommit-timeline check (the structural finding) — container / unauth

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-3-precommit-timelin.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **container** · auth **unauth** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Inventory the pre-round event payloads (`game_starting`, `game_started`, ...). ZERO
hash/seed/commitment fields pre-round = nothing publicly binds the outcome before bets
close. Phrase it precisely: "not verifiable on any publicly-checkable channel" — the
burden of proof inverts to the operator (they claimed PF; the public wire can't show
it). A hash delivered in the SAME event as the outcome is unfalsifiable by construction.

**Semantics check before scoring any pre-round value as a commitment:** verify what the
value MEANS in the game rules, not just that it appears pre-round. Some pre-round values
are the game's public STATE by design — hilo publishes the current reference card
(`apriori {color, number}`) so players can bet higher/lower AGAINST it; calling that an
outcome pre-commit manufactures a fake finding (and the correction later undermines the
whole report). Only a value that binds the OUTCOME (seed/hash/randomness consumed by the
result) counts. Read the game's rules chunk or the operator's PF explainer before rating.

## Probe adjustment (container × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
