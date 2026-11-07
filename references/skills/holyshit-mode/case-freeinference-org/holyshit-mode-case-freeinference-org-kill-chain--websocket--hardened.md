# Kill Chain — websocket / hardened

- source canon: `holyshit-mode/case-freeinference-org.md`
- base technique: `holyshit-mode-case-freeinference-org-kill-chain.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **hardened** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

1. **Recon**: `dig TXT freeinference.org` → no SPF leak. TLS SAN reveals `openinfra.freeinference.org` + `*.opendata.freeinference.org`.
2. **Surface Discovery**: `/api/dashboard` returns 200 unauth with 55KB GPU telemetry (stale cache). JS bundle (`app.js`) reveals two password-gated endpoints:
   - `x-refresh-password` → `/api/dashboard?refresh=1` (cache-bust)
   - `x-export-password` → `/api/export?days=N` (full data export)
3. **Vector**: Both endpoints use single shared secrets, stored in sessionStorage, with **ZERO rate limiting** (20 rapid wrong-password attempts → all 401, zero 429 on each).
4. **Exploitation**: Brute-forced `x-export-password` with trivial wordlist. Password `madsys` matched on 7th attempt.
5. **Exfiltration**: `GET /api/export?days=30` with `x-export-password: madsys` → **6.3MB JSON** of live telemetry. Verified with days=90 (same volume, 720-hour retention).

## Probe adjustment (websocket × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
