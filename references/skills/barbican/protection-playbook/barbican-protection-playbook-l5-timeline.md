# L5 — TIMELINE

- source canon: `barbican/protection-playbook.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Audit | Synthesis |
|---|---|
| engagement pacing patterns (burst = fingerprint) | bursts chunked + paused (same discipline as noise budgets) |
| time-of-day correlation with the operator's routine | schedule around it; the vantage's timezone is the opsec timezone |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
