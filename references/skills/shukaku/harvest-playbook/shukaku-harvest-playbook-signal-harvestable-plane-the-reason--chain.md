# Signal → harvestable plane (the reasoning table) — chain composition

- source canon: `shukaku/harvest-playbook.md`
- base technique: `shukaku-harvest-playbook-signal-harvestable-plane-the-reason.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`reason` matches confirmed access against these signals; each hit becomes a ranked
hypothesis with the exact read-only proof:

| Signal (regex on findings/proofs/ledgers) | Plane | Class | Read-only proof |
|---|---|---|---|
| sql / database / select count | SQL plane | PII | `information_schema.tables` + row counts |
| s3 / bucket / object store / minio | object storage | BACKUP | bucket key inventory + prefixes |
| admin / tenant / saas / export | SaaS admin | SASS | export-config list + member counts |
| repo / source / github | source plane | SRC | repo list + secret-class counts |
| ssh / shell / root / host | host filesystem | CRED | env/cron/keyfile listings (counts) |
| key / secret / token / firmware | keyring/device | CRED | keyring + cert inventories |
| http / url / api / endpoint | harvest surface | BACKUP | GET-only surface probe |
| registered crowns | drift | (same) | re-run the reach proof |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
