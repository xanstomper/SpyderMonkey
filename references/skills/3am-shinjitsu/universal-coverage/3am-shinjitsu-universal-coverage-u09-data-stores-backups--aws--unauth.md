# U09 Data stores & backups — aws / unauth

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u09-data-stores-backups.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **aws** · auth **unauth** · chain role **entry**

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- [ ] Database/search/cache engines, versions, users, TLS, network ACL, and encryption reviewed
- [ ] Object-store policies, bucket ACLs, presigned URL handling, and versioning reviewed
- [ ] Replication, backup encryption, retention, restore test, and deletion protection reviewed
- [ ] Least-privilege application identities and query monitoring verified
- [ ] Data classification and redaction in logs/test evidence enforced

## Probe adjustment (aws × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
