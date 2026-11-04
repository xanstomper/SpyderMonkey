# Confirmed findings — ios / high-priv

- source canon: `holyshit-mode/case-atessa-top.md`
- base technique: `holyshit-mode-case-atessa-top-confirmed-findings.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **ios** · auth **high-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

1. **Pre-auth routing-table oracle (45):** unauth `POST /v1/chat/completions` — AUTH-GATED set (401) = live routes: claude-sonnet-4-6, claude-opus-4-6/4-7/4-8, claude-haiku-4-5-20251001, mai-voice-2, whisper-large-v3-turbo; all others → 503 `No providers available` (auth NEVER checked). Dumps live provider config pre-auth; any future non-gated provider addition is reachable unauth until auth-order is fixed. Whitespace suffix (`"claude-sonnet-4-6 "`) dodged the exact-match gate for some IDs.
2. **forgot-password unthrottled (40):** no captcha, no rate limit (36 rapid 200s @7.5ms), uniform response = no email enumeration but a mail-bomb pump on the target's sender reputation. `/api/auth/resend-verification` same (35).
3. **Public captcha-config:** `/api/public/captcha-config` → `{enabled:true, site_key:"0x4AAAAAADYnNDVbXy5fKK0H"}`. Found via lazy chunk `TurnstileWidget-D1hFjgeC.js` (chunks call public endpoints the main bundle never touches).
4. **count_tokens unthrottled CPU DoS (50):** `POST /v1/messages/count_tokens` (key-auth) — no rate limit (15-burst zero 429, 2.1s), no body-size cap (2.5M-token/5MB body → 200 `input_tokens: 2500003` in 3.27s), 10 parallel 1M-token bodies all processed (CPU-bound 7-10s each, returned 200). Tokenization endpoints are free CPU amplifiers: bounded-test big-body → burst → parallel on any gateway. Fix: per-key rate limit + server-side max input tokens.
5. **429-vs-401 key-validity discriminator:** exhausted key returns 429 `Quota and bonus credits exhausted. Resets 2026-10-07 00:00:00` — proves key live, leaks reset timestamp + quota model, costs nothing. Even 0×-weight "free" models quota-gated (hard enforcement, no bypass).

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
