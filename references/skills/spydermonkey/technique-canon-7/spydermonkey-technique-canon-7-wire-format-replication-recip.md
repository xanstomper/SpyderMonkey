# Wire-format replication recipe

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-06

## The technique

Custom-binary protocol replication (the bc.game t1→/test/→t2 chain): mirror the app's packet TYPES exactly — mis-framing reads as a false gate (the SPY-069 lesson). Decisive test: handshake ACCEPTED with sid issued = protocol replication proven; wrong-ack ≠ server gate.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
