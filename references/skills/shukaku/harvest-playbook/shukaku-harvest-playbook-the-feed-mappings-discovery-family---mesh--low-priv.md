# The feed mappings (discovery → family material) — mesh / low-priv

- source canon: `shukaku/harvest-playbook.md`
- base technique: `shukaku-harvest-playbook-the-feed-mappings-discovery-family-.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **mesh** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

| Discovery | → 3AM row (flaw · seam) | → undercroft | → holyshit |
|---|---|---|---|
| exposed backup/dump (hunt or BACKUP crown) | 13 cloud-misconfig · K cloud-policy | — | recipe card |
| exposed .env/.git/config | 15 database-exposure · G edgefn<->db | CONFIRMED surface | recipe card |
| admin/export reach (SASS crown) | 6 identifier-trust · C auth<->backend-binding | CONFIRMED surface (admin) | — |
| data plane via harvested access (PII/FIN crown) | 15 database-exposure · G edgefn<->db | — | — |
| SRC crown | 2 trust-in-client-params · B client<->server-validation | — | recipe card |
| CRED crown | 10 entropy/forge · C auth<->backend-binding (reuse check) | — | — |

Feed is idempotent per (kind, what, destination) — never double-shipped. Next
steps after feed: `3AM promote --apply --verified` · `kairo ingest --target <t>`.

## Probe adjustment (mesh × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
