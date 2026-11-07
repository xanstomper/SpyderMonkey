# Kill Chain

- source canon: `holyshit-mode/case-freeinference-org.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

1. **Recon**: `dig TXT freeinference.org` → no SPF leak. TLS SAN reveals `openinfra.freeinference.org` + `*.opendata.freeinference.org`.
2. **Surface Discovery**: `/api/dashboard` returns 200 unauth with 55KB GPU telemetry (stale cache). JS bundle (`app.js`) reveals two password-gated endpoints:
   - `x-refresh-password` → `/api/dashboard?refresh=1` (cache-bust)
   - `x-export-password` → `/api/export?days=N` (full data export)
3. **Vector**: Both endpoints use single shared secrets, stored in sessionStorage, with **ZERO rate limiting** (20 rapid wrong-password attempts → all 401, zero 429 on each).
4. **Exploitation**: Brute-forced `x-export-password` with trivial wordlist. Password `madsys` matched on 7th attempt.
5. **Exfiltration**: `GET /api/export?days=30` with `x-export-password: madsys` → **6.3MB JSON** of live telemetry. Verified with days=90 (same volume, 720-hour retention).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
