# Route53/HostedZone and subdomain delegation — chain composition

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-route53-hostedzone-and-subdom.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Route

- probes: `subfinder`, `amass`, `dnsx`, `subzy`, `dnstwist`, `dig-cname`, `dig-axfr`, `nuclei-takeover`, `urlcrazy`, `assetfinder`, `findomain`
- chains: `dns`, `takeover-full`, `osint`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Delegated zones pointing at claimable/dangling NS. Decisive test: NS query chain — NXDOMAIN delegation = the domtake-prep class.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
