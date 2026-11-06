# API batch abuse

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## The technique

Batch/multi-endpoint accepting N operations in one call, bypassing per-op checks. Decisive test: 2-op batch where op-2 alone would 403 = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
