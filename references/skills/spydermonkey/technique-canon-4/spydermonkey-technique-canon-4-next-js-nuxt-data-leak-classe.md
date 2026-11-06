# Next.js/Nuxt data-leak classes

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

_next data payloads leaking props, static export leaking private pages, middleware bypass via _next paths. Decisive test: page props diff for auth-gated routes — private data in the payload = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
