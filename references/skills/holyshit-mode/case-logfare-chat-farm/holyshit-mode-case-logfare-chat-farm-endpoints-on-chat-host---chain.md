# Endpoints on chat host (all Origin-gated, all real JSON) — chain composition

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-endpoints-on-chat-host-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`/api/health {status,version}` · `/api/models` (full tier/visibility/premium intel; leaks hidden default `claude-sonnet-4.5` not in public list) · `/api/chat` · `/api/conversations` (GET list / PATCH / DELETE per-id) · `/api/settings` (GET/PUT) · `/api/consent` (GET: `{tier:"anonymous",can_use_premium:false,logged_in:false}`).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
