# api.gratisfy.xyz gateway (the real prize) — ios / high-priv

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-gateway-mint.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-gateway-mint-api-grat.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **ios** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

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

## Probe adjustment (ios × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
