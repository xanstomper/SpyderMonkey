# Phase 1 — Catalog (reach inventory, read-only) — mesh / federated

- source canon: `shukaku/harvest-playbook.md`
- base technique: `shukaku-harvest-playbook-phase-1-catalog-reach-inventory-rea.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **mesh** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

| Asset class | Reach proof (read-only) | Registered scope |
|---|---|---|
| SQL DB | `SELECT count(*) FROM <table>` with harvested creds | table · row count · schema classes |
| NoSQL | `db.<col>.count()` (operator-owned) | collection · doc count |
| Object store | bucket listing + key count | bucket · key count · prefixes |
| Backups | backup inventory list (glacier/S3/cron/NFS) | artifact · size · freshness |
| SaaS export | tenant admin export config review (read-only list) | tenant · export scope |
| Source repos | repo list + secret scan (operator-owned code) | repos · secret class counts |
| Device/keys | KAIRO findings: key extraction proof (read-only) | key material type · count |

Sample rule: ≤3 rows, redacted at capture, only to prove class — the register keeps
counts and hashes of samples, never contents.

## Probe adjustment (mesh × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
