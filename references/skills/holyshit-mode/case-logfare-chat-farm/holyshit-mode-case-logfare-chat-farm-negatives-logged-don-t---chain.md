# Negatives (logged, don't re-probe) — chain composition

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-negatives-logged-don-t-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Tier-2 consent gate holds: glm-5/grok-4.6 → 403 `consent_required` (real server gate; mass-assigned tier/role/can_use_premium/consent fields accepted `{"ok":true}` but stripped — verify by GET-back + retry, not the 200).
- Cross-session conversation IDOR → 404; client-supplied `conversation_id` ignored; no shared global buffer (PTOK constant 7-36/fresh session, cross-user probe → NONE).
- Model-field path traversal → clean 502 upstream-404 passthrough (no SSRF via model routing).
- SvelteKit escapes stored conversation titles; settings theme not reflected into HTML.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
