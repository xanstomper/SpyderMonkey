# Provably-fair chain verification (decisive-negative)

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- generated: 2026-11-06

## The technique

hash(N-1)=SHA256(hash(N)) across 99 live rounds = committed chain; 0/95 derivations matching your own recomputation = server-secret-backed multiplier (SPY-059). The chain arithmetic IS the finding — no prediction claimed beyond the math.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
