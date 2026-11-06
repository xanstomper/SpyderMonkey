# Breach-history research chain (in order) — ci-cd / unauth

- source canon: `holyshit-mode/breach-regulator-osint.md`
- base technique: `holyshit-mode-breach-regulator-osint-breach-history-research.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- context: **ci-cd** · auth **unauth** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

1. `web_search "<target> hack OR breach OR vulnerability OR exploit"` — the first hit names
   the incident class (hot-wallet key compromise vs smart-contract vs platform/web).
2. Follow the cascade: the wire (CoinDesk, news.bitcoin.com) -> aggregators/loss trackers ->
   forensic blogs. The forensic blogs carry the second-by-second timelines the wire drops:
   drain duration ("hot wallet emptied in 132 seconds" = signing automation, not manual),
   attacker addresses, consolidation addresses, mixer flows, chaser dust (a competitor
   attacker watching the same wallets = the target is under ACTIVE multi-party pressure).
3. Record root-cause status explicitly. "Suspected private-key compromise, no post-mortem
   published" weeks later = the root cause may still be live, and a hastily rebuilt stack
   ("2.0", relaunch in days) = a fresh, unaudited surface. That combination is the highest-
   priority live-engagement brief.
4. Corporate-blog contradictions are findings: "no breach since <year>" claims vs the record;
   license/footer pages naming TWO different legal entities or license numbers on one site =
   ops-hygiene signals and OSINT leads.
5. Repeat for every sibling brand in the fleet — shared infra means one breach = fleet-wide
   exposure, and the smaller brand's incident write-ups often name the shared backend.

## Probe adjustment (ci-cd × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
