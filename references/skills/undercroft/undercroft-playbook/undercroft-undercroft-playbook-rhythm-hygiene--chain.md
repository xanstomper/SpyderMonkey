# Rhythm & hygiene — chain composition

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-rhythm-hygiene.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Seams probed clean: EXHAUSTED with exact test string; never re-fired without a
  change in target state.
- Drift: re-verify before re-asserting a CONFIRMED seam from an earlier session.
- Chunking + noise budgets: family §12; bundles parsed locally, never uploaded.
- PII minimality inherited; samples ≤3, redacted.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
