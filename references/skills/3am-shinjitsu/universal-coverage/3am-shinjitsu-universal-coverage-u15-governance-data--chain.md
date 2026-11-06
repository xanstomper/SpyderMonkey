# U15 Governance & data — chain composition

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u15-governance-data.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- [ ] Data map, classification, residency, retention, encryption, and deletion verified
- [ ] Vendor/third-party access reviewed against least privilege and expiry
- [ ] Backup/DR and incident communication paths tested or tabletop-reviewed
- [ ] Privacy controls for exports, support tooling, and analytics verified
- [ ] Exception register and risk acceptance have owners and expiry dates

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
