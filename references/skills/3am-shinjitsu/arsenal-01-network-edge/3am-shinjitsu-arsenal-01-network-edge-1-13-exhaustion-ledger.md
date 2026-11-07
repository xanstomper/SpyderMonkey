# 1.13 Exhaustion ledger template (class 1)

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

```
{"class":"network/edge","probe":"3306-banner","test":"connect :3306 read greeting",
 "result":"5.5.5-10.1.48-MariaDB","verdict":"CONFIRMED","score":85,
 "next":"searchsploit mariadb 10.1 — documented PoC adaptation only"}

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
