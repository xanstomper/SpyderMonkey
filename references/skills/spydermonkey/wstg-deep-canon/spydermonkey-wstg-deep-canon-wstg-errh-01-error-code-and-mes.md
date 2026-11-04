# WSTG-ERRH-01 Error Code and Message Analysis

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- generated: 2026-11-04

## The technique

- class: stack traces, sql fragments, paths in errors
- probe: malformed inputs forcing 500s on the lab replica; harvest the trace class
- wall: read-only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
