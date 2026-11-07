# 9.3 Forensics cascade (score 70)

- source canon: `3am-shinjitsu/arsenal-09-breach-osint.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Wire → aggregators → forensic blogs: drain timelines, attacker/consolidation addresses,
  mixer flows, chaser dust.
- "No post-mortem published" + rushed rebuilt stack = HIGHEST-priority live brief: root cause
  possibly unfixed; focus the whole engagement on the rebuilt surface.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
