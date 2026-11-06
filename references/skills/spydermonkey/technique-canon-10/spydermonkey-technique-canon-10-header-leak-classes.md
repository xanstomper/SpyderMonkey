# Header-leak classes

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

## The technique

Inbound mail headers revealing internal hostnames/IPs of the estate (your own mailbox). Decisive test: header analysis of a self-sent test = the intel row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
