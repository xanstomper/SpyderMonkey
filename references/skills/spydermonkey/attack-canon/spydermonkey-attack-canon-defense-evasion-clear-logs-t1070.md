# Defense Evasion Clear Logs (T1070)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

- class: log tampering to erase the trail
- probe: NEVER; the estate memory + tamper-evident hash chain exists to resist this
- wall: REFUSED — the ledger is append-only, hash-chained, tamper-evident

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
