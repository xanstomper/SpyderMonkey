# 3. Precommit-timeline check (the structural finding) — chain composition

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-3-precommit-timelin.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
