# 2. Model substitution via `served_by` (score 55)

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

The `served_by` response field reveals actual routing. All `ollama/*` requests
(`llama4`, `qwen3.8`, `gemma4-*`, `qwen3.6-35b`) returned `served_by=ollama/glm-4.7-flash` — the
router sanitizes every ollama submodel to ONE serving model. `model` reported the requested name
but `served_by` showed the real engine. Billing/model-routing flaw (ask for cheap, get fixed
model). Wildcard/empty/default/best/auto model names all 404 → no wildcard routing bypass.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
