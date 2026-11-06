# CRITICAL — Hermes `custom_providers` must be a LIST, not a dict (bit the wiring hard) — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-critical-hermes-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

When adding a local OpenAI-compatible proxy as a Hermes provider:
- `hermes_cli/config.py::get_compatible_custom_providers` does `if not isinstance(custom_providers, list): return []`. If `custom_providers:` under `model:` is written as a **dict** (keyed by provider name), the function bails and returns ONLY the `providers:` entries — your new provider is silently dropped and Hermes falls back to the default provider (whose API-key/502 errors look like YOUR proxy is broken).
- If you add it under BOTH `model.custom_providers` AND top-level `providers:`, the dict under `custom_providers` returns `[]` → the `providers:` dict wins. But a stale entry the dedup keys on (name/url/model triple) can merge/wrong-URL another provider. **Cleanest: register ONLY under the top-level `providers:` key** (a dict, which IS handled) — e.g. `providers: obsidian-free:` with `base_url: http://localhost:8620/v1`, `api_mode: openai`, `api_key`, `model`, `models`. That keyed schema is what the compat view reads.
- **Flat model names vs slashed ids:** the proxy advertises `hyb/kimi-k3` etc. but the upstream *also* accepts slashed ids. Hermes historically struggles with `/` in model ids, so the proxy should expose a flat alias resolver (`kimi-k3` → `hyb/kimi-k3`). Give the proxy a `resolve_model()` that strips the provider prefix.
- **Wire as fallback chain** (`fallback_model:` list of `{provider, model}`) so the free proxy auto-catches when the primary rate-limits/5xxs — zero user action.
- Verify with `hermes -z "prompt" -m <flat> --provider <name>` returning real text, plus a tool-calling run.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
