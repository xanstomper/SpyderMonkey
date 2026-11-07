# App-server fingerprint — chain composition

- source canon: `spydermonkey/technique-canon-11.md`
- base technique: `spydermonkey-technique-canon-11-app-server-fingerprint.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Server header, default error pages, and file extensions fingerprint the tier. Decisive test: three independent signals agreeing = the era-stack row.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
