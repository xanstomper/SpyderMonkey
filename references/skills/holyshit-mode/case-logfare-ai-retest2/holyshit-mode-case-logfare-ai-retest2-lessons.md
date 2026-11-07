# Lessons

- source canon: `holyshit-mode/case-logfare-ai-retest2.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

1. CORS finding severity is a function of auth model + cookie SameSite, not the reflection
   alone. Read raw Set-Cookie flags before rating; re-derive severity when auth model churns.
2. Targets get rebuilt between sessions (SPA → server-rendered). Diff the openapi route list
   across re-engagements like bundle hashes; don't grep a stale bundle.
3. Marketing copy about signup friction is not evidence — probe the register endpoint.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
