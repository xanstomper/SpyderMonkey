# 6. The hardened-auth fingerprint (so you stop and don't brute) — web-app / unauth

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-6-the-hardene.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **unauth** · chain role **entry**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Server-side PKCE Supabase/GoTrue is the OPPOSITE of the gratisfy client-side-exposed version:
- **Zero `createClient`/`anonKey`/`supabase` refs in ANY crawled JS chunk** → anon key never ships
  to the browser; GoTrue signup/verify unreachable keyless.
- **`redirect_to` is hardcoded server-side** in the OAuth authorize URL (every `redirect_to=<evil>`
  override ignored) → no OAuth redirect_uri forge (contrast: gratisfy forwarded verbatim).
- Turnstile on every bootstrap route; opaque DB `session_id`; `spend-unlock` → `no_session`.
When these all hold, say "auth wall hardened, no unauth forge" and move on — do NOT brute or
fabricate a bypass. The real find is then the internal fleet, not the auth stack.

## Probe adjustment (web-app × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
