# Addendum — re-engage #5 (2026-10-06): proxy-fleet build + empty-content hardening

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

The operator shifted from recon to building a USABLE proxy over the unauth `/pg/chat` vector:
`~/obsidian-proxy/obsidian_proxy.py` (port 8620). This is the durable "wrap an unauth upstream
chat vector as a local OpenAI-compatible gateway" pattern (see SKILL.md "Free-AI proxy build
pattern"). Session added:

### Fleet probe discipline
Before wiring anything, live-probe EVERY model in `/v1/models` in parallel (submit with a
`tools` payload). Output per model: does it return real content? does it emit native
`tool_calls`? what `served_by` shows. On obsidian: 30/38 models live, 27 with native
tool-calling — the fleet is mixed. Models that live-probe 502 / empty get pruned, not assumed.

### CRITICAL — Hermes `custom_providers` must be a LIST, not a dict (bit the wiring hard)
When adding a local OpenAI-compatible proxy as a Hermes provider:
- `hermes_cli/config.py::get_compatible_custom_providers` does `if not isinstance(custom_providers, list): return []`. If `custom_providers:` under `model:` is written as a **dict** (keyed by provider name), the function bails and returns ONLY the `providers:` entries — your new provider is silently dropped and Hermes falls back to the default provider (whose API-key/502 errors look like YOUR proxy is broken).
- If you add it under BOTH `model.custom_providers` AND top-level `providers:`, the dict under `custom_providers` returns `[]` → the `providers:` dict wins. But a stale entry the dedup keys on (name/url/model triple) can merge/wrong-URL another provider. **Cleanest: register ONLY under the top-level `providers:` key** (a dict, which IS handled) — e.g. `providers: obsidian-free:` with `base_url: http://localhost:8620/v1`, `api_mode: openai`, `api_key`, `model`, `models`. That keyed schema is what the compat view reads.
- **Flat model names vs slashed ids:** the proxy advertises `hyb/kimi-k3` etc. but the upstream *also* accepts slashed ids. Hermes historically struggles with `/` in model ids, so the proxy should expose a flat alias resolver (`kimi-k3` → `hyb/kimi-k3`). Give the proxy a `resolve_model()` that strips the provider prefix.
- **Wire as fallback chain** (`fallback_model:` list of `{provider, model}`) so the free proxy auto-catches when the primary rate-limits/5xxs — zero user action.
- Verify with `hermes -z "prompt" -m <flat> --provider <name>` returning real text, plus a tool-calling run.

### Reasoning-only empty-content failover (general upstream-proxy hardening)
The biggest "models aren't working in Hermes" trap: upstream returns 200 with non-zero
`completion_tokens` but **`message.content: ""`** — the model burned tokens on the CoT/reasoning
field and never populated `content`. Any client that requires text (Hermes, SDKs) sees an
"empty answer" and looks broken. Two fixes in the proxy:
1. `_salvage_reasoning`: if `content` empty but `reasoning_content`/`reasoning` present, promote
   it to `content` (mark `_from_reasoning`). muse's real answer lives in `reasoning_content`.
2. `_is_empty_completion` must flag empty-`content` even when tokens>0 (`completion_tokens>0`
   is NOT evidence of a usable answer), then fail over to next host / mark model dead (TTL'd)
   rather than serve a blank 200.
3. **Upstream availability churns HARD on free vectors** — a model serving content at 06:00 can
   502/degrade within 15 min. The dead-cache TTL (fail-open: re-probe after TTL, return 200 if
   upstream recovered) is the correct recovery, not a permanent hard-502. Assert that in tests
   (a "model now 200" after a prior fail is the fail-open working, NOT a regression).

### SSE `[DONE]` guarantee
Upstream SSE streams can truncate without `data: [DONE]`. A browser reader loop that waits for
the terminator hangs forever. The proxy's `sse_wrap` must gated-yield `data: [DONE]\n\n` in a
`finally` when the upstream didn't. (For the browser half: a `finalize()` guard that always runs
on stream end / error / catch, so the meta/status line always renders.)

### Raw-string trap in proxied HTML blobs (cost ~2 restarts)
Wrapping the playground HTML in a Python `r"""..."""` raw string to silence a `\s` SyntaxWarning
BREAKS the embedded JS — the JS needs Python `\n` → newline translation for SSE buffer scanning
(`buf.indexOf('\n\n')`), which a raw string turns into literal backslashes. Fix the warning by
escaping the specific JS regex backslashes (`[\s\S]`→`[\\s\\S]`, `<\/think>`→`<\\/think>`) so
Python emits literal single-escapes to the browser, NOT by raw-stringing the whole blob. A
SyntaxWarning on a JS regex inside an HTML string is harmless; don't degrade correctness to
silence it.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
