# vLLM `/scale_elastic_ep` = unauth control-plane write (cost-destruction) — websocket / unauth

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-vll.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **unauth** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

```
POST /scale_elastic_ep  {"new_data_parallel_size": N}
```
- No auth. `N=0` -> 400 "must be a positive integer" (DoS-to-zero blocked at validation).
- `N=1000` -> 500 "Scale failed" (the endpoint really ATTEMPTED the scale -> proves live
  execution, not a stub). `N=1` -> 200 "Scaled...".
- **Proof-of-execution discriminator:** an error from a *post-validation handler* (500/408)
  vs a *validation error* (400/422) proves the endpoint actually reached the backend op.

## Probe adjustment (websocket × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
