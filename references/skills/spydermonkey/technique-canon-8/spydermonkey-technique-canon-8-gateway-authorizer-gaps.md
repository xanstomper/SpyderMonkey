# Gateway authorizer gaps

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

Custom authorizers caching identity by wrong key (the identity-mixup class). Decisive test: two principals sharing a cached response = the finding (your own test pair).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
