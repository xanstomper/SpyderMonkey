# Geoblocking/WAF-tier inconsistency — container / unauth

- source canon: `spydermonkey/technique-canon-7.md`
- base technique: `spydermonkey-technique-canon-7-geoblocking-waf-tier-inconsis.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- context: **container** · auth **unauth** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Differential treatment by region/ASN (the partial-remediation drift class, SPY-096): a 503-gated transport with a still-200 sibling mint = partial closure. Decisive test: same probe, two regions/ASNs on the sanctioned vantages — the matrix is the finding.

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
