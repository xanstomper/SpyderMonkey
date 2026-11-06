# 10.5 Model-substitution oracle (score 75) — mail / unauth

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- base technique: `3am-shinjitsu-arsenal-10-llm-ai-10-5-model-substitution-orac.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- context: **mail** · auth **unauth** · chain role **pivot**

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- `served_by`/upstream headers vs requested model = substitution collapse (pay-for-X,
  served-Y). Client-supplied `system` role honored = stack manipulation primitive.

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
