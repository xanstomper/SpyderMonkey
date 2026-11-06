# Node/Express stack-trace and source disclosure — chain composition

- source canon: `spydermonkey/technique-canon-4.md`
- base technique: `spydermonkey-technique-canon-4-node-express-stack-trace-and-.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Error handlers dumping stack + cwd, sourcemaps (already canon-I), .map on chunk files. Decisive test: forced error on a non-route — stack text with paths = the finding.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
