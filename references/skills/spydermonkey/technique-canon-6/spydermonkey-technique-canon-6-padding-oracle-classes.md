# Padding-oracle classes

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

Distinguishable padding errors (status/length/timing) on ciphertext-bearing params — the lab replica proves the oracle shape; live characterization is ONE probe pair against your own ciphertext. The Manger/Vaudenay recovery itself is never executed live (no-gain).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
