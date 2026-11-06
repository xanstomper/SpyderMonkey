# ERB/Mako/pebble/nunjinjucks

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

`<%= 7*7 %>` (erb), `${7*7}` (mako/pebble/nunjucks ambiguity resolved by error text). Decisive test: marker + engine-error cross-read.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
