# CloudFront behavior gaps

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-06

## The technique

Path-handling divergences (encoding, case) bypassing behavior restrictions at the edge. Decisive test: encoded variant of a restricted path — origin 200 = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
