# CRITICAL — Hermes `custom_providers` must be a LIST, not a dict (bit the wiring hard) — web-app / machine

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-critical-hermes-.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **web-app** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

When adding a local OpenAI-compatible proxy as a Hermes provider:
- `hermes_cli/config.py::get_compatible_custom_providers` does `if not isinstance(custom_providers, list): return []`. If `custom_providers:` under `model:` is written as a **dict** (keyed by provider name), the function bails and returns ONLY the `providers:` entries — your new provider is silently dropped and Hermes falls back to the default provider (whose API-key/502 errors look like YOUR proxy is broken).
- If you add it under BOTH `model.custom_providers` AND top-level `providers:`, the dict under `custom_providers` returns `[]` → the `providers:` dict wins. But a stale entry the dedup keys on (name/url/model triple) can merge/wrong-URL another provider. **Cleanest: register ONLY under the top-level `providers:` key** (a dict, which IS handled) — e.g. `providers: obsidian-free:` with `base_url: http://localhost:8620/v1`, `api_mode: openai`, `api_key`, `model`, `models`. That keyed schema is what the compat view reads.
- **Flat model names vs slashed ids:** the proxy advertises `hyb/kimi-k3` etc. but the upstream *also* accepts slashed ids. Hermes historically struggles with `/` in model ids, so the proxy should expose a flat alias resolver (`kimi-k3` → `hyb/kimi-k3`). Give the proxy a `resolve_model()` that strips the provider prefix.
- **Wire as fallback chain** (`fallback_model:` list of `{provider, model}`) so the free proxy auto-catches when the primary rate-limits/5xxs — zero user action.
- Verify with `hermes -z "prompt" -m <flat> --provider <name>` returning real text, plus a tool-calling run.

## Probe adjustment (web-app × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
