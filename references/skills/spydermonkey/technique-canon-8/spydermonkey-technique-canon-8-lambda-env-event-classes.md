# Lambda env/event classes

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

Function config exposure (env vars in artifacts) and unauth event-ingestion endpoints. Decisive test: config artifact fetch — the plaintext env = the crown.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
