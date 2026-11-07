# Phase 3 — Disclosure map

- source canon: `shukaku/harvest-playbook.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Trigger | Obligation class | Timeline class | Prerequisite |
|---|---|---|---|
| PII breached (US/state) | state AG notification laws | 30d class | investigation complete |
| PII breached (EU) | GDPR Art. 33/34 | 72h class | risk assessment |
| FIN/PCI | card-brand + acquiring bank | immediate class | forensic report |
| Health | HIPAA/HITECH HHS | 60d class | risk assessment |
| Corporate secrecy | contracts/insurance breach clauses | policy class | legal review |
| Backup/ransom-class | extortion-reporting + regulator | 24h class | containment |

The map is a DELIVERABLE for the operator's own org — it names what the company
would owe, it is never used to threaten anyone.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
