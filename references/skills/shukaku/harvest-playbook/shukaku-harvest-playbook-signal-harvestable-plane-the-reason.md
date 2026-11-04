# Signal → harvestable plane (the reasoning table)

- source canon: `shukaku/harvest-playbook.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
