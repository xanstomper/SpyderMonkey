# 2. Model substitution via `served_by` (score 55) — android / machine

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-2-model-substitu.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **android** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

The `served_by` response field reveals actual routing. All `ollama/*` requests
(`llama4`, `qwen3.8`, `gemma4-*`, `qwen3.6-35b`) returned `served_by=ollama/glm-4.7-flash` — the
router sanitizes every ollama submodel to ONE serving model. `model` reported the requested name
but `served_by` showed the real engine. Billing/model-routing flaw (ask for cheap, get fixed
model). Wildcard/empty/default/best/auto model names all 404 → no wildcard routing bypass.

## Probe adjustment (android × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
