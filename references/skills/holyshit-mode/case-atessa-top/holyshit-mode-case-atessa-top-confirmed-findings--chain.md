# Confirmed findings — chain composition

- source canon: `holyshit-mode/case-atessa-top.md`
- base technique: `holyshit-mode-case-atessa-top-confirmed-findings.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. **Pre-auth routing-table oracle (45):** unauth `POST /v1/chat/completions` — AUTH-GATED set (401) = live routes: claude-sonnet-4-6, claude-opus-4-6/4-7/4-8, claude-haiku-4-5-20251001, mai-voice-2, whisper-large-v3-turbo; all others → 503 `No providers available` (auth NEVER checked). Dumps live provider config pre-auth; any future non-gated provider addition is reachable unauth until auth-order is fixed. Whitespace suffix (`"claude-sonnet-4-6 "`) dodged the exact-match gate for some IDs.
2. **forgot-password unthrottled (40):** no captcha, no rate limit (36 rapid 200s @7.5ms), uniform response = no email enumeration but a mail-bomb pump on the target's sender reputation. `/api/auth/resend-verification` same (35).
3. **Public captcha-config:** `/api/public/captcha-config` → `{enabled:true, site_key:"0x4AAAAAADYnNDVbXy5fKK0H"}`. Found via lazy chunk `TurnstileWidget-D1hFjgeC.js` (chunks call public endpoints the main bundle never touches).
4. **count_tokens unthrottled CPU DoS (50):** `POST /v1/messages/count_tokens` (key-auth) — no rate limit (15-burst zero 429, 2.1s), no body-size cap (2.5M-token/5MB body → 200 `input_tokens: 2500003` in 3.27s), 10 parallel 1M-token bodies all processed (CPU-bound 7-10s each, returned 200). Tokenization endpoints are free CPU amplifiers: bounded-test big-body → burst → parallel on any gateway. Fix: per-key rate limit + server-side max input tokens.
5. **429-vs-401 key-validity discriminator:** exhausted key returns 429 `Quota and bonus credits exhausted. Resets 2026-10-07 00:00:00` — proves key live, leaks reset timestamp + quota model, costs nothing. Even 0×-weight "free" models quota-gated (hard enforcement, no bypass).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
