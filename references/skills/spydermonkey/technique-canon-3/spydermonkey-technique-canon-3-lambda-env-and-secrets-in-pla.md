# Lambda/env and secrets-in-plaintext classes

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

Config exposure revealing plaintext env/secrets (e.g. error pages, config endpoints, downloadable artifacts). Decisive test: the artifact's own content — a live secret in a fetched artifact is the crown.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
