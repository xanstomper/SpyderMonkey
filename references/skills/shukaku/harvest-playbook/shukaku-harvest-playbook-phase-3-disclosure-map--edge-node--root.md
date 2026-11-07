# Phase 3 — Disclosure map — edge-node / root

- source canon: `shukaku/harvest-playbook.md`
- base technique: `shukaku-harvest-playbook-phase-3-disclosure-map.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **edge-node** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

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

## Probe adjustment (edge-node × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
