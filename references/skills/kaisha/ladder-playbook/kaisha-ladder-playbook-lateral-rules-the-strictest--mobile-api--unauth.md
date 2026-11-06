# Lateral rules (the strictest) — mobile-api / unauth

- source canon: `kaisha/ladder-playbook.md`
- base technique: `kaisha-ladder-playbook-lateral-rules-the-strictest.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **mobile-api** · auth **unauth** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

1. Own declared estates only — the scope authority (`~/.redteam/scope.json`) is
   checked; out-of-scope hosts refuse.
2. One shot per path per engagement window — never repeated without drift.
3. Nothing persists: no keys copied to disk, no schedules, no implants.
4. Every CONFIRMED lateral → shukaku ingest (the family loop closes).

## Probe adjustment (mobile-api × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
