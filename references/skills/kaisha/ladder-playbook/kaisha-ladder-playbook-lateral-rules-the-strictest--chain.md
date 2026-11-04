# Lateral rules (the strictest) — chain composition

- source canon: `kaisha/ladder-playbook.md`
- base technique: `kaisha-ladder-playbook-lateral-rules-the-strictest.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. Own declared estates only — the scope authority (`~/.redteam/scope.json`) is
   checked; out-of-scope hosts refuse.
2. One shot per path per engagement window — never repeated without drift.
3. Nothing persists: no keys copied to disk, no schedules, no implants.
4. Every CONFIRMED lateral → shukaku ingest (the family loop closes).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
