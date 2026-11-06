# Real campaigns vs engine artifacts — ci-cd / low-priv

- source canon: `spydermonkey/ledger-dump.md`
- base technique: `spydermonkey-ledger-dump-real-campaigns-vs-engine-artifacts.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **ci-cd** · auth **low-priv** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

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

## Probe adjustment (ci-cd × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
