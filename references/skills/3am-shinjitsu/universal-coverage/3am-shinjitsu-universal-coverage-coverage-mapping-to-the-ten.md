# Coverage mapping to the ten surface classes

- source canon: `3am-shinjitsu/universal-coverage.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Existing class | Universal domains |
|---|---|
| 1 Network/Edge | U01, U02 |
| 2 Web app | U03 |
| 3 API | U04 |
| 4 Auth/Identity | U05 |
| 5 Client-side | U06 |
| 6 Infra/Hosting | U07, U08, U09 |
| 7 Supply-chain/Deps | U10 |
| 8 Human/Identity | U11, U12, U16 |
| 9 Breach/OSINT | U01, U10, U11, U14, U15 |
| 10 LLM/AI | U13 |

The universal file expands coverage without weakening the ten-class contract. An
engagement may merge domains in its ledger, but all sixteen must be probed or N/A'd.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
