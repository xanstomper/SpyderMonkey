# API Endpoints Discovered (via /openapi.json)

- source canon: `holyshit-mode/case-logfare-ai.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
