# Debug log exposure

- source canon: `spydermonkey/technique-canon-9.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

debug.log under wp-content readable — its content IS the harvest. Decisive test: fetch with the control-path differential.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
