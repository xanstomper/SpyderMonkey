# Phase 1 — Catalog (reach inventory, read-only) — aws / high-priv

- source canon: `shukaku/harvest-playbook.md`
- base technique: `shukaku-harvest-playbook-phase-1-catalog-reach-inventory-rea.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **aws** · auth **high-priv** · chain role **pivot**

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (aws × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
