# REST view/post-state leak

- source canon: `spydermonkey/technique-canon-9.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

## The technique

Status queries exposing draft/private posts via REST params. Decisive test: your own draft visible unauth = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
