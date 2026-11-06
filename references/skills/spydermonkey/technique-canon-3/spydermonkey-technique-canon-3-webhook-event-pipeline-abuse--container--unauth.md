# Webhook/event pipeline abuse — container / unauth

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-webhook-event-pipeline-abuse.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **container** · auth **unauth** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Unsigned or replayable events (the SPY-102 class family) — event-name freedom + spoofed actor ids poisoning downstream automation. Decisive test: accepted event with a spoofed field on a test endpoint — the acceptance is the finding.

## Probe adjustment (container × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
