# Gopher/dict protocol handlers

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-INPV-10** · **CWE-918** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

Legacy URL handlers turn SSRF into protocol talk. Decisive test: a gopher CRLF payload reaching an internal listener you control — handler presence = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
