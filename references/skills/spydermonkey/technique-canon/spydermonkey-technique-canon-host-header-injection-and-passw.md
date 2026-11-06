# Host-header injection and password-reset poisoning

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

## The technique

Host header reaching generated links/emails/redirects. Decisive test: Host=your.domain on a state-changing POST — the generated URL in the response/email carries your host = the finding (pairs with the reset class).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
