# SAML per-profile depth

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## The technique

Web-SSO signature wrapping (canon-I), ECP/Artifact-profile residue, metadata trust reuse across SPs. Decisive test: metadata parse + one wrapped-assertion acceptance on your test SP.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
