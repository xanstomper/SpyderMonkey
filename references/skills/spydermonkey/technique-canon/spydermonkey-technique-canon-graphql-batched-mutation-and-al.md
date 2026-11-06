# GraphQL batched-mutation and alias abuse

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-APIT-10** · **CWE-1321** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

Batched operations/aliases bypass per-field rate logic. Decisive test: 10 aliased identical mutations in one request on a test object — 10 executions = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
