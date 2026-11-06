# Shipping and tax zeroing

- source canon: `spydermonkey/technique-canon.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- generated: 2026-11-06

## The technique

The shipping/tax line recomputed per address/region can be zeroed by a region string the tax table lacks. Decisive test: region=XX-UNKNOWN at checkout — total drops the tax line = the finding (characterize, don't purchase).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
