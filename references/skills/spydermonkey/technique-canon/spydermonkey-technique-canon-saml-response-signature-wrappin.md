# SAML response signature wrapping

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## The technique

Multiple assertion signatures or an unsigned assertion beside a signed one let a wrapping attack move the subject. Decisive test: duplicate the assertion with a wrapped subject and observe acceptance — acceptance of ANY forged assertion is confirmed; the account used must be your own test principal.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
