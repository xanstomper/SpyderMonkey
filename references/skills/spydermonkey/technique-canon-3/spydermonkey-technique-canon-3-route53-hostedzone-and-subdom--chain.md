# Route53/HostedZone and subdomain delegation — chain composition

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-route53-hostedzone-and-subdom.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Delegated zones pointing at claimable/dangling NS. Decisive test: NS query chain — NXDOMAIN delegation = the domtake-prep class.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
