# REPLAY — webhook, replay, idempoten, callback, dedup — mobile / unauth

- source canon: `kairo/technique-classes.md`
- base technique: `kairo-technique-classes-replay-webhook-replay-idempoten-call.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **mobile** · auth **unauth** · chain role **pivot**

## Context

- platform: family probes cover the class
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- REPLAY
- webhook, replay, idempoten, callback, dedup
- 5/B
- STATE

## Probe adjustment (mobile × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
