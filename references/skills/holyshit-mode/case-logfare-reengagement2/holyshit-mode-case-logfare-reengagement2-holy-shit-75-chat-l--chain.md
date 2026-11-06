# HOLY SHIT (75): chat.logfare.ai anon inference farm — chain composition

- source canon: `holyshit-mode/case-logfare-reengagement2.md`
- base technique: `holyshit-mode-case-logfare-reengagement2-holy-shit-75-chat-l.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Chain: `Origin: https://chat.logfare.ai` header (plain spoof) → `POST /api/chat {"message":...,
"model":"logfare/auto"}` → server mints `lfc_session` (90-day HttpOnly) with zero auth → real
SSE completions. ~30 reqs, zero 429s; 3 parallel long completions (1.7k/1k/2.7k tokens) served.

Key discriminators learned:
- **Origin gate is a header string-match, enforced only at SESSION MINT.** evil/null/absent →
  403 during mint; once a session cookie exists, the same POST works with **no Origin at all**.
  Test the gate separately for mint vs. use — one 403 does not mean the endpoint is gated.
- **Playground hosts hide the real API.** Ghost discrimination on chat host: `404 text/html` =
  ghost, `403 application/json` = real route. Found `/api/health`, `/api/models`,
  `/api/chat`, `/api/auth`, `/api/conversations`, `/api/settings`, `/api/consent`.
- **Error channel gives body shape:** bare POST → 400 "message required" (field is `message`,
  not OpenAI `messages`).
- **SSE is base64-wrapped JSON per `data:` line** (`eyJ...`) — decode with `+ '='*(-len%4)`;
  `logfare_complete:true` final chunk carries usage. First-chunk `usage.prompt_tokens` is the
  PTOK-drift oracle (constant ~7-36/fresh session here = isolated sessions, no shared buffer).
- **Anon `/api/settings` PUT accepts `system_prompt`/`default_model` (persisted) but mass-assigned
  `tier/role/premium/consent` fields are silently dropped** — server re-checks tier on every call
  (`consent_required` 403 on tier-2 models). `/api/consent` GET leaks `{"tier":"anonymous",
  "can_use_premium":false,"logged_in":false}`.
- **Conversation IDOR held** (cross-session read → 404). PATCH/DELETE own conversation 200.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
