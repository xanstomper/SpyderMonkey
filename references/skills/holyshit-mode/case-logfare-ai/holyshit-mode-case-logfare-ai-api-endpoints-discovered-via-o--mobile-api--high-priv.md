# API Endpoints Discovered (via /openapi.json) — mobile-api / high-priv

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-api-endpoints-discovered-via-o.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mobile-api** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (mobile-api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
