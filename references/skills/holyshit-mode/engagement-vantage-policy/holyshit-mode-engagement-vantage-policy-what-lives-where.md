# What lives where

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- VM (`ssh vermes`, opc@92.5.99.31): `~/holyshit-mode/` (full repo) + `~/.hermes/scripts/holyleadger/` (all 15 ledger JSONs, chmod 700 dir / 600 files).
- Home: same paths (authoritative copy for git pushes — VM has no GitHub creds).
- Sync out: `rsync -az ~/holyshit-mode/ vermes:~/holyshit-mode/` + ledger dir.
- Sync back: reverse rsync after engagement, then relay to GitHub from home.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
