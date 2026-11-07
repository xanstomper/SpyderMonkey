# Rate-limit architecture classes

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Header-trust (canon-I), per-route vs global buckets, burst-then-sustain shapes observable from response headers (Retry-After, X-RateLimit-*). Decisive test: header telemetry over N paced requests — the bucket model is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
