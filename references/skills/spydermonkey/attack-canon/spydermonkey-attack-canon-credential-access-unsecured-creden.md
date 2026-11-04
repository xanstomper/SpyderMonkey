# Credential Access Unsecured Credentials (T1552)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-04

## The technique

- class: keys/secrets in files, env, registries, object storage
- probe: read-only harvest scans (`.env`, `.git`, backup dumps, bucket listings)
- wall: NO-GAIN — found secrets are redacted in the ledger, never reused

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
