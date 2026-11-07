# The auth-stack hardening that refutes "just forge a session" (adjacent, 2026-10-14) — worker / machine

- source canon: `holyshit-mode/llm-gateway-ssrf-oracle-and-drain-calibration.md`
- base technique: `holyshit-mode-llm-gateway-ssrf-oracle-and-drain-calibration-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **worker** · auth **machine** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (worker × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
