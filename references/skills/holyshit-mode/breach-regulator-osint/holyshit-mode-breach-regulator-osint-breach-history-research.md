# Breach-history research chain (in order)

- source canon: `holyshit-mode/breach-regulator-osint.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- generated: 2026-11-04

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
