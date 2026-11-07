# The auth-stack hardening that refutes "just forge a session" (adjacent, 2026-10-14) — graphql / unauth

- source canon: `holyshit-mode/llm-gateway-ssrf-oracle-and-drain-calibration.md`
- base technique: `holyshit-mode-llm-gateway-ssrf-oracle-and-drain-calibration-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **graphql** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Do not assume an OAuth gateway can be session-forged. On a **server-side-PKCE Supabase/GoTrue** gateway:
- the **anon key never ships to the browser** (0 `supabase` refs in all bundles) — can't hit GoTrue
  signup/verify keyless;
- **`redirect_to` is hardcoded server-side** (all override attempts ignored) — not the example-target
  open-redirect forge;
- Turnstile gates `/auth/create-account`, `/auth/otp`, `/auth/password/signin`; `spend-unlock` is
  session-gated; every `/api/*` is 401.
Classify such a stack as "no unauth auth-wall bypass" with evidence (redirect hardcode + no anon key)
rather than re-running capture-gated signup loops.

## Probe adjustment (graphql × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
