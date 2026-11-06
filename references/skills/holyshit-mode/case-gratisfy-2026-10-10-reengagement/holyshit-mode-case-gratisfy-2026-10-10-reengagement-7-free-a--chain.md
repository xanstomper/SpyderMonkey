# 7. FREE AI media proxy — no email verify, no turnstile, no sk_ key (score 95, TOP FINDING) — chain composition

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-reengagement-7-free-a.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`chat.gratisfy.xyz` with `X-Chat-Auth-Mode: account` + Bearer <unverified session>:
- `POST /api/media/audio/speech` {model:google-ai-studio/gemini-2.5-flash-preview-tts, input, voice} → 200, real WAV
- `POST /api/media/images/generations` {model:cloudflare/@cf/black-forest-labs/flux-1-schnell, prompt} → 200, 1024x1024 PNG
- `POST /api/media/audio/transcriptions` (multipart file= + model=google-ai-studio/gemini-2.5-flash) → **Gemini 2.5 Flash VLM answers image questions** — free vision-model access
- TEXT chat (`/api/chat`) IS turnstile-gated ("Human verification required... Gratisfy-provided model") and `/v1/*` needs sk_ — the media pipeline is the hole.
- Rate limit ~6 req/min/account → defeated by minting more phone accounts (2s each, rotation confirmed working).
- Dead upstreams: unorouter (401), vercel (404) — use google-ai-studio / cloudflare models.
- Call-shape: headers Content-Type/Authorization/X-Chat-Auth-Mode:account/X-Website-Route: chat-app; model needs `provider/` prefix or errors `missing_provider`.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
