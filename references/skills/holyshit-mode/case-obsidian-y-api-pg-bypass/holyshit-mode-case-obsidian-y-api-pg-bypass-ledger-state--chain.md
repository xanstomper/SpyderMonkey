# Ledger state — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api-pg-bypass.md`
- base technique: `holyshit-mode-case-obsidian-y-api-pg-bypass-ledger-state.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`holyleadger` target `obsidian-y-api-r4xe.onrender.com`:
- `pg_chat_unauthenticated_free_ai` confirmed score 90
- `pg_chat_no_rate_limit` confirmed score 70
- `pg_hidden_50k_system_prompt` hypothesis score 55 (decisive next: reasoning-field extraction)
- `pg_stream_passthrough` confirmed score 35
- Chain: `free_ai_abuse`: pg_chat_no_auth → unlimited_completions → no_rate_limit →
  free_upstream_inference (confirmed)

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
