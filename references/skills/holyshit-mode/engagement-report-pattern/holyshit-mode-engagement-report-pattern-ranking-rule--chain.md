# Ranking rule — chain composition

- source canon: `holyshit-mode/engagement-report-pattern.md`
- base technique: `holyshit-mode-engagement-report-pattern-ranking-rule.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`confirmed(3) > inconclusive(2) > hypothesis(1) > negative(0)`, then score desc within a
tier. Implemented as `sorted(classes.items(), key=lambda kv: (-rank(status), -score))`.
Confirmed classes always outrank hypotheses even if the hypothesis has a higher raw score —
a proven finding is worth more than an unproven high-scoring guess.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
