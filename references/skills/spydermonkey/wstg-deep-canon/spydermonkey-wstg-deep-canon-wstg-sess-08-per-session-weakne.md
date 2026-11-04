# WSTG-SESS-08 Per-Session Weakness

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

- class: same session id across concurrent logins (non-unique)
- probe: two parallel logins on the lab replica, diff ids
- wall: lab replica

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
