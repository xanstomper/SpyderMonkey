# Dangling CNAME / subdomain takeover — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-dangling-cname-subdomain-takeov.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

CNAME to NXDOMAIN + claimable service = takeover prep. Decisive test: cname → resolution failure + the target service's fingerprint (e.g. "There isn't a GitHub Pages site here") = the class. Register the claimability, never claim a third-party domain you lack rights to.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
