# Initial Access Valid Accounts (T1078)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **PTES-PE** · **CWE-522** · **ATT&CK T1555**
- generated: 2026-11-04

## The technique

- class: default/leaked/reused credentials
- probe: only credentials the SCOPE FILE declares; never a live brute against prod
- wall: brute classes run against the dojo replica; prod runs are refusals

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
