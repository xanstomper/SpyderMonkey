# Per-domain decisive tests — the compromise battery — chain composition

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-per-domain-decisive-tests-t.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The checklists above are the audit pass. THIS is the exploitation pass: for every
U-domain, the decisive tests that prove actual control on authorized targets.
Each is minimal, read-only or one-request, documented-PoC adaptation only (§15).
Score §14 before running; ledger every negative with its exact test. A positive
triggers OP-ESCALATE (hunt the consumer) immediately.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
