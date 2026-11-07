# Route53/HostedZone and subdomain delegation

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## Route

- probes: `subfinder`, `amass`, `dnsx`, `subzy`, `dnstwist`, `dig-cname`, `dig-axfr`, `nuclei-takeover`, `urlcrazy`, `assetfinder`, `findomain`
- chains: `dns`, `takeover-full`, `osint`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Delegated zones pointing at claimable/dangling NS. Decisive test: NS query chain — NXDOMAIN delegation = the domtake-prep class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
