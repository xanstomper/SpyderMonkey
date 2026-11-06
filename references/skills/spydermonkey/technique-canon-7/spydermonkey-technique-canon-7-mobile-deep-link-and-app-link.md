# Mobile deep-link and app-link hijack (depth)

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **MASTG-PLATFORM** · **CWE-927** · **ATT&CK T1546**
- generated: 2026-11-06

## The technique

App-links without domain verification (assetlinks absent) = hijack-prep. Decisive test: the verification file's absence on the domain — 404/missing = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
