# IAM assume-role trust exposure

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-06

## The technique

Role trust policies naming external accounts/wildcards (read-only via your own principal's visibility). Decisive test: trust policy document fetch where permitted — the wildcard = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
