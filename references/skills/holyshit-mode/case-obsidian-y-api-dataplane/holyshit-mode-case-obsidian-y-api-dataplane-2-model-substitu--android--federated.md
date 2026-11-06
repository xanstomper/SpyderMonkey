# 2. Model substitution via `served_by` (score 55) — android / federated

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-2-model-substitu.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **android** · auth **federated** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

The `served_by` response field reveals actual routing. All `ollama/*` requests
(`llama4`, `qwen3.8`, `gemma4-*`, `qwen3.6-35b`) returned `served_by=ollama/glm-4.7-flash` — the
router sanitizes every ollama submodel to ONE serving model. `model` reported the requested name
but `served_by` showed the real engine. Billing/model-routing flaw (ask for cheap, get fixed
model). Wildcard/empty/default/best/auto model names all 404 → no wildcard routing bypass.

## Probe adjustment (android × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
