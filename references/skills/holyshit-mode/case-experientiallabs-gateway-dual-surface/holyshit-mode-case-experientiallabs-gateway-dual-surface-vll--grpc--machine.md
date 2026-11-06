# vLLM `/scale_elastic_ep` = unauth control-plane write (cost-destruction) — grpc / machine

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-vll.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **grpc** · auth **machine** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

```
POST /scale_elastic_ep  {"new_data_parallel_size": N}
```
- No auth. `N=0` -> 400 "must be a positive integer" (DoS-to-zero blocked at validation).
- `N=1000` -> 500 "Scale failed" (the endpoint really ATTEMPTED the scale -> proves live
  execution, not a stub). `N=1` -> 200 "Scaled...".
- **Proof-of-execution discriminator:** an error from a *post-validation handler* (500/408)
  vs a *validation error* (400/422) proves the endpoint actually reached the backend op.

## Probe adjustment (grpc × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
