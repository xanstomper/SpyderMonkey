# WSTG Input Validation Testing (WSTG-INPT)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- generated: 2026-11-04

## The technique

- class: injection families — sql, ldap, xss, xxe, ssti, cmd, deserialization
- probe: the 14-marker INJECTION battery + 8-encoding traversal battery
- wall: reflected/evaluated markers only; never destructive payloads

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
