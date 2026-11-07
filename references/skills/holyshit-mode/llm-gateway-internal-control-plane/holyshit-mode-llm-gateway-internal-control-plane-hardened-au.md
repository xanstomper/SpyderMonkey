# Hardened-auth negatives (don't waste time — these are the STRONG parts)

- source canon: `holyshit-mode/llm-gateway-internal-control-plane.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
