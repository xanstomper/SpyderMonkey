# 9.1 Breach-context search (score 80)

- source canon: `3am-shinjitsu/arsenal-09-breach-osint.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-07

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `web_search <target> breach leak ransomware` + ransomware.live + Breachsense-class trackers
  + news. Corroborate what the victim CONFIRMED ("withdrawal requests were added to the
  database" = proven DB-write access) before theorizing.
- FULL WORKED CASE: `case-example-target-adjacent-infra.md` (holyshit refs, normative by reference).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
