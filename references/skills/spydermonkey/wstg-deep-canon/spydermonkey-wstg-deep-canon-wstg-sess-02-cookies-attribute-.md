# WSTG-SESS-02 Cookies Attribute Flags

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

- class: missing Secure/HttpOnly/SameSite on session cookies
- probe: Set-Cookie header inventory across the lab replica's flows
- wall: read-only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
