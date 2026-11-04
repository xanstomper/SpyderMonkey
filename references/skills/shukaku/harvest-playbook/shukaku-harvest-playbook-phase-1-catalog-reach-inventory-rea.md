# Phase 1 — Catalog (reach inventory, read-only)

- source canon: `shukaku/harvest-playbook.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
