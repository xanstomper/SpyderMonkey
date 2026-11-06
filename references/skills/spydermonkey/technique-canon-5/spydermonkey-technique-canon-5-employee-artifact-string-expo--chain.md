# Employee/artifact-string exposure (zero-document boundary) — chain composition

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-employee-artifact-string-expo.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Public artifact strings (git emails, doc metadata) — barbican's protect/sanitize canon applied OFFENSIVELY as recon: what does the ESTATE leak about itself. Decisive test: the string source URL — each leak is a row. Zero-document rule: no people-targeting, estate-artifacts only.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
