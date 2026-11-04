# Phase 3 — Disclosure map — chain composition

- source canon: `shukaku/harvest-playbook.md`
- base technique: `shukaku-harvest-playbook-phase-3-disclosure-map.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
