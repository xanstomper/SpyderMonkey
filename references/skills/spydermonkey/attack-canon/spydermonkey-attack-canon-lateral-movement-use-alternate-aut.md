# Lateral Movement Use Alternate Authentication Material (T1550)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

- class: pass-the-hash/ticket, session hijack
- probe: session-id enumeration class only (sequential/weak ids — CWE-384)
- wall: the SESSION tester proves structure weakness; no replay against prod

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
