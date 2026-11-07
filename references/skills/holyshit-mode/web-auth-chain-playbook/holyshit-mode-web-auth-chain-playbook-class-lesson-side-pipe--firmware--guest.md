# Class lesson: side-pipeline trust split (session-verified 2026-10-10, g***REDACTED***.xyz) — firmware / guest

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-class-lesson-side-pipe.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **firmware** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

Platforms gate the FLAGSHIP endpoint (text chat, `/v1/*`) hard while SISTER pipelines sharing the
same session trust root stay open. g***REDACTED***.xyz: text chat turnstile-gated, `/v1` needed an sk_
key — but `chat.g***REDACTED***.xyz/api/media/*` (speech/images/transcriptions) accepted the SAME
unverified phone session with `X-Chat-Auth-Mode: account` + `X-Website-Route: chat-app`, no
turnstile, no email verification → free Gemini TTS (WAV), free FLUX images (1024px PNG), and a
free Gemini 2.5 Flash VLM via the transcriptions multipart endpoint (send an image file with a
`prompt=` field). Rule: once you hold ANY session, enumerate every `X-*-Mode` header family (the
400 error names the modes) and test each mode against EVERY endpoint family, not just the one the
SPA uses. Model IDs need `provider/` prefix. Rate limits (~6 req/min) fall to free phone-account
rotation. Always test asset download unauthenticated — `/media/assets/ast_<hex>` served 200 with
zero auth (IDOR).

## Probe adjustment (firmware × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
