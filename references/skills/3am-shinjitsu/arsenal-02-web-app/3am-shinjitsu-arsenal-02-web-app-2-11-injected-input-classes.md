# 2.11 Injected-input classes (score per-cell, from vector-matrix B)

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- One decisive probe per class, on ONE parameter, once: SQLi (error/boolean/time), NoSQLi
  (`{"$ne":null}` in JSON fields), SSTI (`{{7*7}}` in rendered/report fields), path traversal
  (`../%2e%2e` on filename/range/zip-entry), open redirect (`//evil`, `/\evil`, `@evil`),
  prototype pollution (`__proto__` in JSON merges), XXE (OOB DNS canary only).
- CONFIRMED WHEN: oracle in response (diff, error, canary callback). No spraying: one param,
  one class, one probe; a twice-failed approach is dead.
- CSV/formula injection in export features (`=cmd`); webhooks unsigned/replayable.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
