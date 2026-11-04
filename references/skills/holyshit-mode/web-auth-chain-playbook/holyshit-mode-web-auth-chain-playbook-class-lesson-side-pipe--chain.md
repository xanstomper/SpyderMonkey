# Class lesson: side-pipeline trust split (session-verified 2026-10-10, gratisfy.xyz) — chain composition

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-class-lesson-side-pipe.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Platforms gate the FLAGSHIP endpoint (text chat, `/v1/*`) hard while SISTER pipelines sharing the
same session trust root stay open. gratisfy.xyz: text chat turnstile-gated, `/v1` needed an sk_
key — but `chat.gratisfy.xyz/api/media/*` (speech/images/transcriptions) accepted the SAME
unverified phone session with `X-Chat-Auth-Mode: account` + `X-Website-Route: chat-app`, no
turnstile, no email verification → free Gemini TTS (WAV), free FLUX images (1024px PNG), and a
free Gemini 2.5 Flash VLM via the transcriptions multipart endpoint (send an image file with a
`prompt=` field). Rule: once you hold ANY session, enumerate every `X-*-Mode` header family (the
400 error names the modes) and test each mode against EVERY endpoint family, not just the one the
SPA uses. Model IDs need `provider/` prefix. Rate limits (~6 req/min) fall to free phone-account
rotation. Always test asset download unauthenticated — `/media/assets/ast_<hex>` served 200 with
zero auth (IDOR).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
