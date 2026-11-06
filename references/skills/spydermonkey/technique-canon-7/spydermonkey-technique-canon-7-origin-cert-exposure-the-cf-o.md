# Origin-cert exposure (the CF Origin Cert class)

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## The technique

Origin certs naming OTHER domains installed on the same box = tri-brand shared origin (SPY-012). Decisive test: TLS handshake cert chain on the ORIGIN IP — foreign SANs = the crown.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
