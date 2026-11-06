# Azure blob anonymous access — container / unauth

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-azure-blob-anonymous-access.md`
- bindings: **PTES-CON** · **CWE-250** · **ATT&CK T1611**
- context: **container** · auth **unauth** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Container-level public access (list/get). Decisive test: anonymous LIST on the container endpoint — the listing is the finding.

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
