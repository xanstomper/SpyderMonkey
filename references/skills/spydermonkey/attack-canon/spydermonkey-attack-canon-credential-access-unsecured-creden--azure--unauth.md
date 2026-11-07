# Credential Access Unsecured Credentials (T1552) — azure / unauth

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-credential-access-unsecured-creden.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **azure** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: keys/secrets in files, env, registries, object storage
- probe: read-only harvest scans (`.env`, `.git`, backup dumps, bucket listings)
- wall: NO-GAIN — found secrets are redacted in the ledger, never reused

## Probe adjustment (azure × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
