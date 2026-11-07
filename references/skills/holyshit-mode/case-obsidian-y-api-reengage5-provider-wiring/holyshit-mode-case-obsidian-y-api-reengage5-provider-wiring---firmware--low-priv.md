# Hermes wiring — THE custom_providers DICT GOTCHA — firmware / low-priv

- source canon: `holyshit-mode/case-obsidian-y-api-reengage5-provider-wiring.md`
- base technique: `holyshit-mode-case-obsidian-y-api-reengage5-provider-wiring-.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **firmware** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

`get_compatible_custom_providers()` in hermes_cli/config.py:
```python
custom_providers = config.get("custom_providers")
if custom_providers is not None:
    if not isinstance(custom_providers, list):
        return []        # <-- dict-form custom_providers = ALL providers silently dropped
```
Symptom: new provider 401s against a DIFFERENT host (Hermes fell back to the default provider;
the "$1.00 testing balance" error body was freeinference's, not the proxy's). Fix: register
under top-level `providers:` keyed schema (api_key/api_mode/base_url/key_env/model/name/models
with per-model context_length). Verify resolution:
```python
from hermes_cli.config import load_config, get_compatible_custom_providers
[print(p.get('provider_key'), p.get('base_url')) for p in get_compatible_custom_providers(load_config())]
```
Hermes invocation: `hermes -z "..." -m glm-4.7-flash --provider obsidian-free`.
Fallback chain: `fallback_model: [{provider, model}, ...]` in config.yaml (hermes fallback shows it).
Verified end-to-end: -z prompt returns; full agent tool round-trip (model calls terminal tool,
returns exact echo output) through the free proxy.

## Probe adjustment (firmware × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
