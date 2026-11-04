# Verification

- source canon: `holyshit-mode/engagement-report-pattern.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- generated: 2026-11-04

## The technique

`report` is verified (a) in-module with an isolated temp ledger seeded with mixed
confirmed/hypothesis/negative + one chain, asserting: rc 0, all six sections present,
score-desc ordering, accurate counts line, chain steps + impact rendered, `--out` writes
a file; and (b) as a subprocess CLI (`holyleadger.py report --target --out`) writing to an
isolated dir. The CI workflow's ledger smoke step ALSO runs `report` and greps for the
"Confirmed Holy Shits" section + a known class name, so a broken report fails the build.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
