# Azure IMDS and SAS-token exposure

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## The technique

IMDS (169.254.169.254/metadata/instance) and SAS tokens in client code (long-lived, broad-scope). Decisive test: metadata response fields; SAS token parsed for scope/expiry — an unexpired broad token in client JS is the crown.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
