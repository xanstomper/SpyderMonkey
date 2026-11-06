# Nuxt payload/SSR leaks

- source canon: `spydermonkey/technique-canon-9.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

## The technique

window.__NUXT__ carrying internal state. Decisive test: payload parse on your own session = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
