# Remediation

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

1. Rate-limit password-gated endpoints (lockout after 5 failed attempts)
2. Per-user auth tokens instead of shared secrets
3. MFA for export/refresh operations
4. Gate the unauthenticated dashboard (55KB stale telemetry leak without auth is itself an info-disclosure)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
