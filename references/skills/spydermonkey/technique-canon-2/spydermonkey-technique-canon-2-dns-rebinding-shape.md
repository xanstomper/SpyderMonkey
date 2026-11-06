# DNS rebinding shape

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

TOCTOU between resolve and fetch — characterized in the lab replica (rebinding needs your own authoritative DNS). The live test registers the TOCTOU hypothesis with the fetch-time evidence you can observe.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
