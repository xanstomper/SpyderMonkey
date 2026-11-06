# API version shadowing

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## The technique

`/api/v2` allowing what v1 patched (or v0/internal still live). Decisive test: same request across version prefixes — a privilege delta across versions is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
