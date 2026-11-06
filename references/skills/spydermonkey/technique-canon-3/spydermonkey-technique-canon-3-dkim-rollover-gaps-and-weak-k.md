# DKIM rollover gaps and weak keys

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- generated: 2026-11-06

## The technique

Stale selectors, sub-1024 keys, missing rotation. Decisive test: selector enumeration + published-key parse — key size is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
