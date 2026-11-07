# Class lesson: side-pipeline trust split (session-verified 2026-10-10, example-target.xyz) — mobile / root

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-class-lesson-side-pipe.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **mobile** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the client is another principal — storage/permission surface, own device only
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

Platforms gate the FLAGSHIP endpoint (text chat, `/v1/*`) hard while SISTER pipelines sharing the
same session trust root stay open. example-target.xyz: text chat turnstile-gated, `/v1` needed an sk_
key — but `chat.example-target.xyz/api/media/*` (speech/images/transcriptions) accepted the SAME
unverified phone session with `X-Chat-Auth-Mode: account` + `X-Website-Route: chat-app`, no
turnstile, no email verification → free Gemini TTS (WAV), free FLUX images (1024px PNG), and a
free Gemini 2.5 Flash VLM via the transcriptions multipart endpoint (send an image file with a
`prompt=` field). Rule: once you hold ANY session, enumerate every `X-*-Mode` header family (the
400 error names the modes) and test each mode against EVERY endpoint family, not just the one the
SPA uses. Model IDs need `provider/` prefix. Rate limits (~6 req/min) fall to free phone-account
rotation. Always test asset download unauthenticated — `/media/assets/ast_<hex>` served 200 with
zero auth (IDOR).

## Probe adjustment (mobile × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
