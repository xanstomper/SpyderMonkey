# Phase 2 — Valuation (the extortion-economy ladder) — chain composition

- source canon: `shukaku/harvest-playbook.md`
- base technique: `shukaku-harvest-playbook-phase-2-valuation-the-extortion-eco.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
