# 4. ★ Media-endpoint oracle bypass (the big one) — chain composition

- source canon: `holyshit-mode/web-llm-proxy-auth-bypasses.md`
- base technique: `holyshit-mode-web-llm-proxy-auth-bypasses-4-media-endpoint-o.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

When the main chat endpoint (`/api/chat`) is gated by turnstile/"human verification":
- The MEDIA endpoints (`/api/media/audio/transcriptions`, `/speech`, `/images/generations`)
  often skip the chat gate AND the email-verification middleware.
- `/api/media/audio/transcriptions` is frequently a GENERIC any-file→model proxy:
  send a TEXT FILE as `file=@/tmp/q.txt;type=text/plain` + `model=<provider/model>` and the
  model answers the question as text. Full completions, code gen, reasoning all work.
- Verified live: Gemini 3.5 Flash text/vision (image upload + question), Cloudflare
  FLUX-1-schnell 1024px images, Google TTS → WAV. All with an UNVERIFIED session, no API key.
- Headers: `X-Chat-Auth-Mode: account` + `X-Website-Route: chat-app` + Bearer session.
- Model catalog: unauth `GET /api/models/bootstrap` lists everything (provider, id,
  modalities, freeTier). Filter `outputModalities` to find image/audio/text models.
- Failures to expect: `unsupported_provider` (bad model prefix format — use `provider/model`),
  upstream 401/404 for providers whose keys are dead (unorouter), `turnstile_required` only
  on Gratisfy-PROVIDED chat models (media path exempt).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
