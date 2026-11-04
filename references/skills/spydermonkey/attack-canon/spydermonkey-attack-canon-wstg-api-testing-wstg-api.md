# WSTG API Testing (WSTG-API)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-APIT-10** · **CWE-1321** · **ATT&CK T1190**
- generated: 2026-11-04

## The technique

- class: graphql introspection, mass assignment, rate limits, versioning
- probe: the MASSASSIGN POST battery + graphql alias/batch checks
- wall: documented classes; no data modification beyond the proof request

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
