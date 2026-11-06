# SQLi time-based discipline

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

SLEEP/BENCHMARK probes at ONE request per measurement, never a burst — a time-based confirmation is a timing histogram over 3 samples against a baseline 3, not a flood.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
