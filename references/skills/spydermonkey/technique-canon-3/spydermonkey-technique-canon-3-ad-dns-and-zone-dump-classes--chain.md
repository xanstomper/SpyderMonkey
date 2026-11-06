# AD DNS and zone dump classes — chain composition

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-ad-dns-and-zone-dump-classes.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

DNS rpc/dll class zones readable anonymously (the recon layer of AD). Decisive test: zone listing — host inventory = the finding.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
