# Null-session enumeration

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

samr/querydominfo/userlist via null session — the inventory IS the finding. Decisive test: rpcclient/smbclient anonymous listing (read-only).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
