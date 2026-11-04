# Score: 92 (High)

- source canon: `holyshit-mode/case-freeinference-org.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- generated: 2026-11-04

## The technique

- **E** (Exploitability): 9 — trivial wordlist brute, no tooling required
- **I** (Impact): 9 — full infra topology + live utilization + traffic volumes
- **L** (Likelihood): 8 — password `madsys` found on 7th attempt; real password likely equally weak
- **R** (Reproducibility): 9 — single curl with correct password returns 6.3MB
- **N** (Novelty): 7 — shared-secret telemetry endpoint is a distinct pattern, but brute-without-rate-limit is classic OWASP

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
