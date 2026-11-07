# Real campaigns vs engine artifacts

- source canon: `spydermonkey/ledger-dump.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`~/.redteam/campaigns/` also holds bench/training/debug dirs that are NOT
engagements: `bdbg*, cdbg*, dbg2, rp, tr-dbg, training, smk-*, bench*, wb, cr2,
surf, sc, demo, ci, klab, klab2, bcgame, nonexistent-zzz, http-127.0.0.1-9,
protect, perabet-funnel, bench-live`. Real engagements carry SPY- rows in a
>3KB ledger.jsonl and/or `*-report.md` / `war-report-*.md` artifacts:
`bc.game, gamdom, ggpoker, oncasi, iceposeidon, rainbet.com, csgoempire`.
Heuristic: real = ledger.jsonl >~3KB with rows whose id starts `SPY-`,
or a war/report artifact present. Engagement names (`klab`, `ggpoker`) are
scope.json fields, NOT the same as campaign dir names.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
