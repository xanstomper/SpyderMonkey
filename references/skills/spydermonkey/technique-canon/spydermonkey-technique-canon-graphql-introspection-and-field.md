# GraphQL introspection and field suggestion

- source canon: `spydermonkey/technique-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

Introspection enabled (or disabled-but-suggested via DidYouMean errors) maps the full schema. Decisive test: introspection query 200 with schema JSON = surface map; wrong-field error naming the right field = suggestion leak.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
