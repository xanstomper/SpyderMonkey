# IAM trust and policy enumeration (read-only) — chain composition

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-iam-trust-and-policy-enumerat.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Instance-profile metadata, `iam:GetUser`-class self-inventory, and policy documents readable with the caller's own context. Decisive test: the account's OWN permissions page/API — inventory of what the foothold can see, never a privilege walk.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
