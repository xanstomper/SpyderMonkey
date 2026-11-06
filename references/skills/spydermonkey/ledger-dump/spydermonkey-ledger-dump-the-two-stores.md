# The two stores

- source canon: `spydermonkey/ledger-dump.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-06

## The technique

1. **Holyleadger** — `~/.hermes/scripts/holyleadger/<domain>.json`, one file per TARGET DOMAIN.
2. **Campaign ledgers** — `~/.redteam/campaigns/<target>/ledger.jsonl`, one per CAMPAIGN DIR.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
