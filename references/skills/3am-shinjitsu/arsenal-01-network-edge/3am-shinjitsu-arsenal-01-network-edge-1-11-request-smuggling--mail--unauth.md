# 1.11 Request-smuggling differential (score 55) [owned infra only] — mail / unauth

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-11-request-smuggling.md`
- bindings: **WSTG-ADV-02** · **CWE-444** · **ATT&CK T1190**
- context: **mail** · auth **unauth** · chain role **pivot**

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- ONE CL.TE differential probe max; timing-only. Any ambiguity = stop, document, never iterate.
- Serverless/CDN-fronted (no dual proxy layer) = N/A — say once, pivot.

## Probe adjustment (mail × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
