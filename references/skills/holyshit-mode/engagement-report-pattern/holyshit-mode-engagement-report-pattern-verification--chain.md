# Verification — chain composition

- source canon: `holyshit-mode/engagement-report-pattern.md`
- base technique: `holyshit-mode-engagement-report-pattern-verification.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`report` is verified (a) in-module with an isolated temp ledger seeded with mixed
confirmed/hypothesis/negative + one chain, asserting: rc 0, all six sections present,
score-desc ordering, accurate counts line, chain steps + impact rendered, `--out` writes
a file; and (b) as a subprocess CLI (`holyleadger.py report --target --out`) writing to an
isolated dir. The CI workflow's ledger smoke step ALSO runs `report` and greps for the
"Confirmed Holy Shits" section + a known class name, so a broken report fails the build.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
