# Signal → harvestable plane (the reasoning table) — gateway / machine

- source canon: `shukaku/harvest-playbook.md`
- base technique: `shukaku-harvest-playbook-signal-harvestable-plane-the-reason.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **gateway** · auth **machine** · chain role **final**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (gateway × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
