# Hardcoded key inventory

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- generated: 2026-11-06

## The technique

API keys/signing secrets embedded in binary or resources. Decisive test: string scan pairing the key with its live use-site = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
