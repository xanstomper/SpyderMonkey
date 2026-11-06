# Jinja2 and Jinja-flavored arithmetic

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## The technique

`{{7*7}}`→49, `{{7*'7'}}`→7777777 fingerprints jinja2; `{{config}}` exposure = the crown. Decisive test: arithmetic marker reflected exactly.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
