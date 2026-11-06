# XInclude and SOAP param XXE

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-INPV-07** · **CWE-611** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

Client-side XML parsers (XInclude on a fragment, SOAP body param) carry the same entity class without a full document control. Decisive test: the OOB marker through the fragment param.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
