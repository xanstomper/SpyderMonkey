# Trial reset and signup-limit bypass

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- generated: 2026-11-06

## The technique

Trial entitlement tied to a client-controllable identity fragment (device id, email alias) is a logic seam. Decisive test: second trial via email+1 alias on your OWN address — entitlement granted = the finding (the abuse class, not the grant).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
