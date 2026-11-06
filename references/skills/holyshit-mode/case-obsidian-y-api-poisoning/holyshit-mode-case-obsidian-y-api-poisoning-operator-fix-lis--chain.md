# Operator fix list (delivered) — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api-poisoning.md`
- base technique: `holyshit-mode-case-obsidian-y-api-poisoning-operator-fix-lis.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. Per-user/per-session conversation state (random session key per browser or no history); flush the poisoned buffer on deploy. Collapses findings 95/85.
2. Session-gate + IP rate-limit /pg/*. Collapses 90/70.
3. Move character/persona data out of system prompt into per-request injection.
4. Auth-gate /status?json=1.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
