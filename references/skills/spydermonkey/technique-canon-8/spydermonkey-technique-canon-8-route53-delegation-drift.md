# Route53 delegation drift

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-07

## Route

- probes: `subfinder`, `amass`, `dnsx`, `subzy`, `dnstwist`, `dig-cname`, `dig-axfr`, `nuclei-takeover`, `urlcrazy`, `assetfinder`, `findomain`
- chains: `dns`, `takeover-full`, `osint`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Hosted-zone records pointing at retired/dead targets (the domtake-prep class). Decisive test: record-by-record resolution sweep = the inventory.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
