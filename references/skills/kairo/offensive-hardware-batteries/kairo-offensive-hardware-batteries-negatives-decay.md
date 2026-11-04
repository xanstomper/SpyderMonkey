# Negatives & decay

- source canon: `kairo/offensive-hardware-batteries.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

- Negatives are results — exact test string in the ledger, never re-probed without a
  change (firmware version, access level, new kit).
- Findings decay: firmware updates kill rollback findings; radio state drifts; cloud
  trust changes. Re-verify before citing.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
