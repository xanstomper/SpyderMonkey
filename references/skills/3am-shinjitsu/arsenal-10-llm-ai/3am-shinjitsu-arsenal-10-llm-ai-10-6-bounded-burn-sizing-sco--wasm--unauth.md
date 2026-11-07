# 10.6 Bounded-burn sizing (score 70, OWNED gateways) — wasm / unauth

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- base technique: `3am-shinjitsu-arsenal-10-llm-ai-10-6-bounded-burn-sizing-sco.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **wasm** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- count_tokens/no-limit endpoints = free CPU-DoS primitive: big body → burst → parallel.
  MEASURE: single 2.5M-token body 3.27s CPU; 10× parallel 1M-token = 7-10s each. Extrapolate
  $/hr exposure from the measurement. Fix: per-key limit + input cap.
- 429-vs-401 discriminator: quota-exhausted key → 429 naming reset ts = key live + quota
  model leak, zero spend.

## Probe adjustment (wasm × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
