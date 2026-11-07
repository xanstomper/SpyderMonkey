# API Endpoints Discovered (via /openapi.json) — chain composition

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-api-endpoints-discovered-via-o.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- /v1/auth/discord/start — Discord OAuth start
- /v1/auth/discord/callback — Discord OAuth callback
- /v1/auth/discord/membership/check — Check Discord membership
- /v1/auth/register — Register (requires Discord)
- /v1/auth/login — Login
- /v1/auth/logout — Logout
- /v1/auth/me — Get current user
- /v1/sso/approve — SSO approve
- /v1/sso/token — SSO token exchange
- /v1/auth/regenerate-key — Regenerate API key
- /v1/auth/consent — Update consent
- /v1/auth/eval-preference — Eval preference
- /v1/auth/training-preference — Training opt-in
- /v1/me/data — DSAR export
- /v1/me/delete — DSAR delete
- /v1/me/opt-out — DSAR opt-out
- /v1/chat/completions — Chat
- /v1/completions — Text completion
- /v1/messages — Anthropic messages
- /v1/responses — OpenAI responses
- /v1/images/generations — Image gen
- /v1/videos/generations — Video gen
- /v1/images/edits — Image edit
- /v1/audio/speech — TTS
- /v1/audio/transcriptions — STT
- /v1/embeddings — Embeddings
- /v1/models — List models
- /v1/status — Model status
- /v1/status/history — Status history

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
