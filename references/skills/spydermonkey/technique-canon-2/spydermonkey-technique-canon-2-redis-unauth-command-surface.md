# Redis unauth command surface

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

INFO/CONFIG GET unauth = exposure class; never SET/DEL. Decisive test: INFO server on 6379 — the response body is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
