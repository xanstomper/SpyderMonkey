# 10.6 Bounded-burn sizing (score 70, OWNED gateways) — ios / machine

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- base technique: `3am-shinjitsu-arsenal-10-llm-ai-10-6-bounded-burn-sizing-sco.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **ios** · auth **machine** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- count_tokens/no-limit endpoints = free CPU-DoS primitive: big body → burst → parallel.
  MEASURE: single 2.5M-token body 3.27s CPU; 10× parallel 1M-token = 7-10s each. Extrapolate
  $/hr exposure from the measurement. Fix: per-key limit + input cap.
- 429-vs-401 discriminator: quota-exhausted key → 429 naming reset ts = key live + quota
  model leak, zero spend.

## Probe adjustment (ios × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
