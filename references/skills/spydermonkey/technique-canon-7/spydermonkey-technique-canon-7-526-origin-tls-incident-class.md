# 526/origin-TLS incident classes

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-06

## The technique

CF 526 on a valid-edge-cert host = broken ORIGIN TLS (the KYC/file-tier incident). Decisive test: edge vs origin handshake comparison — the origin chain is the evidence.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
