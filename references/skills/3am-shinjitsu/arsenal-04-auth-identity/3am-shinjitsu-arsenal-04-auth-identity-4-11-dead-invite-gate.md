# 4.11 Dead-invite gates (score 60)

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## The technique

- Invite-accept signatures: `?invite=<token>` acceptance is client- or server-checked?
  Expired-but-valid-shaped token behavior; enumeration oracle on 404-vs-410.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
