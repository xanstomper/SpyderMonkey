# LDAP anonymous and rootDSE recon

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-06

## The technique

Anonymous binds revealing naming contexts, schema, and object classes. Decisive test: rootDSE fetch — the disclosure depth is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
