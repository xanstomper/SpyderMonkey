# The auth-stack hardening that refutes "just forge a session" (adjacent, 2026-10-14)

- source canon: `holyshit-mode/llm-gateway-ssrf-oracle-and-drain-calibration.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

Do not assume an OAuth gateway can be session-forged. On a **server-side-PKCE Supabase/GoTrue** gateway:
- the **anon key never ships to the browser** (0 `supabase` refs in all bundles) — can't hit GoTrue
  signup/verify keyless;
- **`redirect_to` is hardcoded server-side** (all override attempts ignored) — not the gratisfy
  open-redirect forge;
- Turnstile gates `/auth/create-account`, `/auth/otp`, `/auth/password/signin`; `spend-unlock` is
  session-gated; every `/api/*` is 401.
Classify such a stack as "no unauth auth-wall bypass" with evidence (redirect hardcode + no anon key)
rather than re-running capture-gated signup loops.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
