# U09 Data stores & backups — chain composition

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u09-data-stores-backups.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- [ ] Database/search/cache engines, versions, users, TLS, network ACL, and encryption reviewed
- [ ] Object-store policies, bucket ACLs, presigned URL handling, and versioning reviewed
- [ ] Replication, backup encryption, retention, restore test, and deletion protection reviewed
- [ ] Least-privilege application identities and query monitoring verified
- [ ] Data classification and redaction in logs/test evidence enforced

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
