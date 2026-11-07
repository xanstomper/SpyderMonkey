# Remediation

- source canon: `holyshit-mode/case-freeinference-org.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

1. **Rate-limit** `/api/export` and `/api/dashboard?refresh=1` — lockout after 5 failed password attempts
2. **Replace shared secret** `madsys` with per-user tokens or session-based auth
3. **Add MFA** for refresh/export operations
4. **Restrict unauthenticated `/api/dashboard`** (returns stale cache anyway — gate it)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
