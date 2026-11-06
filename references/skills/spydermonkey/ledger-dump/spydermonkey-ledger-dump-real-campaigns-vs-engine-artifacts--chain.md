# Real campaigns vs engine artifacts — chain composition

- source canon: `spydermonkey/ledger-dump.md`
- base technique: `spydermonkey-ledger-dump-real-campaigns-vs-engine-artifacts.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`~/.redteam/campaigns/` also holds bench/training/debug dirs that are NOT
engagements: `bdbg*, cdbg*, dbg2, rp, tr-dbg, training, smk-*, bench*, wb, cr2,
surf, sc, demo, ci, klab, klab2, bcgame, nonexistent-zzz, http-127.0.0.1-9,
protect, perabet-funnel, bench-live`. Real engagements carry SPY- rows in a
>3KB ledger.jsonl and/or `*-report.md` / `war-report-*.md` artifacts:
`bc.game, gamdom, ggpoker, oncasi, iceposeidon, rainbet.com, csgoempire`.
Heuristic: real = ledger.jsonl >~3KB with rows whose id starts `SPY-`,
or a war/report artifact present. Engagement names (`klab`, `ggpoker`) are
scope.json fields, NOT the same as campaign dir names.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
