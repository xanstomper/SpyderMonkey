# Phase 2 — Valuation (the extortion-economy ladder)

- source canon: `shukaku/harvest-playbook.md`
- bindings: **WSTG-BUSL-01** · **CWE-1336** · **ATT&CK T1565**
- generated: 2026-11-04

## The technique

ESTIMATE ranges per record/asset, labeled with basis. Prices are ranges, never false
precision:

| Class | Basis (observed market) | Range (ESTIMATE) |
|---|---|---|
| PII — US consumer | ~$5–15/record street, breach-class aggregation multipliers | per 1k rows |
| PII — EU (GDPR-class) | higher penalty-weight, lower street | per 1k rows |
| FIN (cards/banking) | $20–50/record class | per record |
| CRED (secrets/keys) | credential-market tiers by privilege | per credential |
| BACKUP (unencrypted dump) | lump: % of org revenue-class (ransom demand logic) | per artifact |
| SRC (exclusive repo) | private repo market + IP class | per repo |
| SASS (tenant export) | SaaS-resale/takeover ladder | per tenant |

Valuation MUST be labeled: `$ESTIMATE (basis: <market-ladder | disclosed demand |
industry benchmark>)`. No invented precision; a single-number price without basis
is a violation.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
