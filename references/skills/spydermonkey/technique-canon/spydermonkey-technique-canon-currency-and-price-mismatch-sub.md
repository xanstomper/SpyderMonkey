# Currency and price-mismatch substitution

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- generated: 2026-11-06

## The technique

A client-supplied currency code (or price object) re-priced by the server at a stale rate is a rounding/repricing seam. Decisive test: switch currency mid-checkout and diff the converted line prices against the live FX the page displays — persistent mismatch = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
