# Rounding-difference accrual

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- generated: 2026-11-06

## The technique

Per-line rounding (banker's vs half-up) accumulated over many lines differs from the total the user authorized. Decisive test: 100-line synthetic cart, server total vs sum-of-lines — the diff is the accounting class ( dojo replica reproduces the arithmetic).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
