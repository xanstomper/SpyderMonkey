# 7. FREE AI media proxy — no email verify, no turnstile, no sk_ key (score 95, TOP FINDING) — android / machine

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-reengagement-7-free-a.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **android** · auth **machine** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

`chat.gratisfy.xyz` with `X-Chat-Auth-Mode: account` + Bearer <unverified session>:
- `POST /api/media/audio/speech` {model:google-ai-studio/gemini-2.5-flash-preview-tts, input, voice} → 200, real WAV
- `POST /api/media/images/generations` {model:cloudflare/@cf/black-forest-labs/flux-1-schnell, prompt} → 200, 1024x1024 PNG
- `POST /api/media/audio/transcriptions` (multipart file= + model=google-ai-studio/gemini-2.5-flash) → **Gemini 2.5 Flash VLM answers image questions** — free vision-model access
- TEXT chat (`/api/chat`) IS turnstile-gated ("Human verification required... Gratisfy-provided model") and `/v1/*` needs sk_ — the media pipeline is the hole.
- Rate limit ~6 req/min/account → defeated by minting more phone accounts (2s each, rotation confirmed working).
- Dead upstreams: unorouter (401), vercel (404) — use google-ai-studio / cloudflare models.
- Call-shape: headers Content-Type/Authorization/X-Chat-Auth-Mode:account/X-Website-Route: chat-app; model needs `provider/` prefix or errors `missing_provider`.

## Probe adjustment (android × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
