# 4. ★ Media-endpoint oracle bypass (the big one)

- source canon: `holyshit-mode/web-llm-proxy-auth-bypasses.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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
  on example-target-PROVIDED chat models (media path exempt).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
