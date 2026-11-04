# WSTG-SESS-03 Session Fixation

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- class: session id accepted BEFORE authentication (fixation class)
- probe: pre-auth token vs post-auth token differential on the lab replica
- wall: lab replica

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
