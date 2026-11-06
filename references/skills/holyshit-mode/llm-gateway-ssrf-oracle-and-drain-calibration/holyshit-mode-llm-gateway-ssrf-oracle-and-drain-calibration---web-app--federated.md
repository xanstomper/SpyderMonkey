# The auth-stack hardening that refutes "just forge a session" (adjacent, 2026-10-14) — web-app / federated

- source canon: `holyshit-mode/llm-gateway-ssrf-oracle-and-drain-calibration.md`
- base technique: `holyshit-mode-llm-gateway-ssrf-oracle-and-drain-calibration-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **federated** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

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

## Probe adjustment (web-app × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
