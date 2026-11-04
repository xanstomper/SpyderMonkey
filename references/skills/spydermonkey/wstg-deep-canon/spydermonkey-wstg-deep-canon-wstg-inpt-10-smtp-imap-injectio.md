# WSTG-INPT-10 SMTP/IMAP Injection

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- generated: 2026-11-04

## The technique

- class: header injection into mail flows
- probe: CRLF markers in the lab replica's mailer form
- wall: lab replica; no real mail is ever sent

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
