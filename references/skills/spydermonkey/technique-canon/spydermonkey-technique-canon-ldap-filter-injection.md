# LDAP filter injection

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

(&(objectClass=*)) metachar reflection into an LDAP filter. Decisive test: value=*)(uid=* — a changed result count = filter injection.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
