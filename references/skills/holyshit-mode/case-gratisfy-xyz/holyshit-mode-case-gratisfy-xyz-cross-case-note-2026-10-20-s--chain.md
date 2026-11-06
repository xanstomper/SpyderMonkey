# Cross-case note (2026-10-20, somny.xyz) — chain composition

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-cross-case-note-2026-10-20-s.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Recurring reseller pattern (gratisfy, gonka, somny): **key-create endpoints return masked keys; a `reveal`/`secret` sub-endpoint is the real primitive** (somny: `POST /api/keys` → masked `sk-som...wle0`, `POST /api/keys/{id}/reveal` → full key). IDOR on reveal with foreign UUID → 400 body-validation (auth checked before existence). Also recurring: disposable-domain signup filters miss mail.tm's rotating domains — probe mail.tm `/domains` for newly-active ones first. See `references/case-somny-xyz.md`.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
