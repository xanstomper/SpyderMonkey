# 4. ★ Media-endpoint oracle bypass (the big one) — wireless / low-priv

- source canon: `holyshit-mode/web-llm-proxy-auth-bypasses.md`
- base technique: `holyshit-mode-web-llm-proxy-auth-bypasses-4-media-endpoint-o.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **wireless** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: LAB-ONLY — your own radios and stations; third-party airwaves are the absolute wall
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

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
  on Gratisfy-PROVIDED chat models (media path exempt).

## Probe adjustment (wireless × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
