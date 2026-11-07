# Hardened Auth-Wall Fingerprint (Supabase/GoTrue server-side PKCE) — does NOT inherit the weak variant

- source canon: `holyshit-mode/hardened-gateway-internal-fleet-proto-surface.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Anon key is **not client-exposed**: OAuth `authorize` to `*.supabase.co/auth/v1/authorize` happens
  **server-side** (server initiates PKCE); zero `supabase`/`eyJ` anon-key in all fetched bundles. GoTrue
  `/auth/v1/*` keyless → `401 No API key found`.
- **`redirect_to` is hardcoded server-side**; override attempts (`https://evil`, `//evil`,
  `javascript:`, legit) are ignored. The gratisfy GoTrue redirect_uri-override forge does NOT apply.
  Fingerprint: `sb-<ref>-auth-token-code-verifier` PKCE cookie + `code_challenge_method=s256`.
- **Turnstile gates every bootstrap** (`/auth/otp`, `/auth/create-account`, `/auth/password/signin` →
  `captcha_failed` 403). Send an empty body to enumerate required fields before captcha blocks.
- **`/auth/spend-unlock`** (card-gate / $1-verify bypass route) is session-gated → `401 no_session`.
- Management API (`/api/orgs/<id>/usage/*`, `/api/keys`, `/api/admin/access`, `/api/account/mfa`)
  returns 401 server-side for every crafted org UUID/numeric id → no IDOR.

**Rule:** when the target is this well-hardened, the auth wall is NOT the vulnerability. State it
plainly, record the negative, pivot to (a) the internal-fleet proto surface above or (b) an
authenticated context from the operator.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
