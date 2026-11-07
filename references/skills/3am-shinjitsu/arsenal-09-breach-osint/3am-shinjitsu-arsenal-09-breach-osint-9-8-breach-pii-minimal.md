# 9.8 Breach PII minimality

- source canon: `3am-shinjitsu/arsenal-09-breach-osint.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-07

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Sample ≤3 rows to prove access, redact at capture, never exfiltrate corpora. The verdict
  needs the PROOF, not the PII.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
