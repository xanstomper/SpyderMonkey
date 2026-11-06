# Edge-worker injection surface

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

Worker scripts reading request material into responses (the SDK class at edge tier). Decisive test: passive capture of the worker's transforms = the map.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
