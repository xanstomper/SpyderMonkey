# api.gratisfy.xyz gateway (the real prize) — chain composition

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-gateway-mint.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-gateway-mint-api-grat.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Discovered by grepping the **platform SPA bundle** (`/assets/platform-*.js`) for hosts:
  `api.gratisfy.xyz` runs a native OpenAI-compatible gateway (`/v1/chat/completions`,
  `/v1/models`, `/v1/responses`, `/v1/embeddings`, `/v1/rerank`, `/v1/images/generations`).
  Earlier conclusion "api host only serves /v1/*, different origin stack" was correct but the
  key to reach it was missing — the SPA was the map.
- 17 `crax-gpt/*` models, free. Live-fire 11/17: claude-opus-5, gpt-6-astra, grok-4-6,
  deepseek-v4-pro, kimi-k3, gpt-5-6-sol, gpt-5-5, claude-sonnet-5, claude-fable-5-1,
  gemini-3-8-flash-crax, instant. Dead upstream: glm-5.3/-flash (Z.ai `USER_BLOCKED`),
  kimi-k2-6 (blank output). **Provider-side streaming broken** ("invalid JSON payload" from
  their SSE path) — non-streaming fine.
- **Native tool calling works** (real `tool_calls` + `finish_reason:tool_calls` on opus-5) —
  no shim needed, unlike the transcription-oracle path.
- Rate limit: **5 req/10s and 20 req/60s per IP** (provider-enforced, not per-key). Bursts
  502/429; space calls 12s apart in verify loops.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
