# Route53 delegation drift

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-06

## The technique

Hosted-zone records pointing at retired/dead targets (the domtake-prep class). Decisive test: record-by-record resolution sweep = the inventory.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
