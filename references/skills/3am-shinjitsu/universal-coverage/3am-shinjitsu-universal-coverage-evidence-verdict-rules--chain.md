# Evidence & verdict rules — chain composition

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-evidence-verdict-rules.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **CONFIRMED** requires an authorized, minimal, non-destructive proof and a control check.
- **BLOCKED** means authorization, vantage, or tooling stopped the decisive test; name it.
- **HYPOTHESIS** means reasoned but unproven; include the exact gap and unlock condition.
- **N/A** requires a concrete reason (e.g. "no AI components deployed; inventory export
  dated 2026-11-03 confirms zero inference endpoints").
- Secrets are redacted in reports. Read-only access is used only to prove impact.
- Findings decay; record deployed version/build and re-verify before reuse.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
