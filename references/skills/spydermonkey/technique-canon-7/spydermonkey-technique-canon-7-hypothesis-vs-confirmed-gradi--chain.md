# Hypothesis-vs-CONFIRMED grading — chain composition

- source canon: `spydermonkey/technique-canon-7.md`
- base technique: `spydermonkey-technique-canon-7-hypothesis-vs-confirmed-gradi.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

No baseline/attack/diff = HYPOTHESIS conf 0.4, never suppressed, never CONFIRMED. Decisive test: the row's status field matches the evidence it carries — the grading integrity check.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
