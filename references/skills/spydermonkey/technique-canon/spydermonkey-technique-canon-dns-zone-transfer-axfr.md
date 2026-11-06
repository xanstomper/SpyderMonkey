# DNS zone transfer (AXFR)

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-06

## The technique

AXFR against all nameservers for the domain. Decisive test: full zone listing from ANY nameserver = the finding (read-only inventory).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
