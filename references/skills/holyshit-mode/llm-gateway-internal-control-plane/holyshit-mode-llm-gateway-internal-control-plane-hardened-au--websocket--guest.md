# Hardened-auth negatives (don't waste time — these are the STRONG parts) — websocket / guest

- source canon: `holyshit-mode/llm-gateway-internal-control-plane.md`
- base technique: `holyshit-mode-llm-gateway-internal-control-plane-hardened-au.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **guest** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

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

## Probe adjustment (websocket × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
