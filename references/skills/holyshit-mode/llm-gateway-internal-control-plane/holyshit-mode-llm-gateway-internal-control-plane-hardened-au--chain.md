# Hardened-auth negatives (don't waste time — these are the STRONG parts) — chain composition

- source canon: `holyshit-mode/llm-gateway-internal-control-plane.md`
- base technique: `holyshit-mode-llm-gateway-internal-control-plane-hardened-au.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

When the platform's auth is well-built, the following are dead ends CONFIRMED live:
- **Supabase/GoTrue server-side PKCE**: OAuth forwards to `https://<proj>.supabase.co/auth/v1/
  authorize` **from the server**, and the **anon key NEVER ships to the browser** (zero refs in
  every JS chunk). You CANNOT reach `/auth/v1/settings`/signup/verify keyless. Don't hunt the
  anon key in the bundle — it isn't there.
- **`redirect_to` hardcoded server-side**: 4 override attempts (https://evil, //evil, javascript:,
  a legit URI) are all ignored; the authorize URL always carries the fixed
  `redirect_to=https://<app>/auth/callback?next=%2F`. NOT the GoTrue `redirect_uri`-forward flaw.
- **Turnstile on every bootstrap** (`/auth/otp`, `/auth/create-account`, `/auth/password/signin`
  → `captcha_failed`) and **opaque DB session cookies** (`session_id`, not a forgeable JWT).
  Staging may be even tighter (`?error=staff_only`).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
