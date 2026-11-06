# Tomcat manager and examples residue — ci-cd / unauth

- source canon: `spydermonkey/technique-canon-4.md`
- base technique: `spydermonkey-technique-canon-4-tomcat-manager-and-examples-r.md`
- bindings: **PTES-PE** · **CWE-522** · **ATT&CK T1555**
- context: **ci-cd** · auth **unauth** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

/manager/html, /host-manager, /examples residue with default or weak gate. Decisive test: HTTP 401-vs-404 classification (401 = surface exists — the inventory finding), never a credential push.

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
