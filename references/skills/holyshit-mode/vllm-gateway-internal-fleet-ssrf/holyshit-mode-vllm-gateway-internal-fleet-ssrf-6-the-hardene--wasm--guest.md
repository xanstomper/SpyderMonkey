# 6. The hardened-auth fingerprint (so you stop and don't brute) — wasm / guest

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-6-the-hardene.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **wasm** · auth **guest** · chain role **entry**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

Server-side PKCE Supabase/GoTrue is the OPPOSITE of the g***REDACTED*** client-side-exposed version:
- **Zero `createClient`/`anonKey`/`supabase` refs in ANY crawled JS chunk** → anon key never ships
  to the browser; GoTrue signup/verify unreachable keyless.
- **`redirect_to` is hardcoded server-side** in the OAuth authorize URL (every `redirect_to=<evil>`
  override ignored) → no OAuth redirect_uri forge (contrast: g***REDACTED*** forwarded verbatim).
- Turnstile on every bootstrap route; opaque DB `session_id`; `spend-unlock` → `no_session`.
When these all hold, say "auth wall hardened, no unauth forge" and move on — do NOT brute or
fabricate a bypass. The real find is then the internal fleet, not the auth stack.

## Probe adjustment (wasm × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
