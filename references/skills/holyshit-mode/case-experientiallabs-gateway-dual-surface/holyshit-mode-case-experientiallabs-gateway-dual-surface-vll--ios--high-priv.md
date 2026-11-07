# vLLM `/invocations` = keyless free-AI inference (payment-gate bypass) — ios / high-priv

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-vll.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **ios** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

```
POST https://wm.xplabs.ai/invocations  {"prompt":"...","model":"claude-opus-5","stream":true}
-> 200 SSE completion, NO KEY
```
- Bypasses the `requires_payment` gate on the whole paid catalog; serves premium models
  (`claude-opus-5`, `deepseek-r1`) keylessly. `stream:true` => drop-in OpenAI-compatible.
- **Model substitution confirm:** requested `deepseek-v4-flash`, got served by
  `glm-5.3-flash-abliterated` (uncensored model rides the shared worker).
- `/invocations` takes ANY known catalog slug; not validated against a single lane's set.

## Probe adjustment (ios × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
