# 6. The hardened-auth fingerprint (so you stop and don't brute) — chain composition

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-6-the-hardene.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Server-side PKCE Supabase/GoTrue is the OPPOSITE of the gratisfy client-side-exposed version:
- **Zero `createClient`/`anonKey`/`supabase` refs in ANY crawled JS chunk** → anon key never ships
  to the browser; GoTrue signup/verify unreachable keyless.
- **`redirect_to` is hardcoded server-side** in the OAuth authorize URL (every `redirect_to=<evil>`
  override ignored) → no OAuth redirect_uri forge (contrast: gratisfy forwarded verbatim).
- Turnstile on every bootstrap route; opaque DB `session_id`; `spend-unlock` → `no_session`.
When these all hold, say "auth wall hardened, no unauth forge" and move on — do NOT brute or
fabricate a bypass. The real find is then the internal fleet, not the auth stack.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
