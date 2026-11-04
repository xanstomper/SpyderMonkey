# Proxy upgrades (~/obsidian-proxy/obsidian_proxy.py)

- source canon: `holyshit-mode/case-obsidian-y-api-reengage5-provider-wiring.md`
- bindings: **WSTG-ADV-01** · **CWE-444** · **ATT&CK T1190**
- generated: 2026-11-04

## The technique

- `resolve_model()`: flat alias → slashed upstream id (Hermes chokes on slashed ids; bare
  `kimi-k3` maps to `hyb/kimi-k3` by suffix match over the model list).
- Dead-model pruning: 502/404 → cache model→ts, typed `proxy_model_dead` 502, hidden from
  `/v1/models`, TTL 900s so redeploys recover.
- Tool-capability tracking: server learns from real responses, exposes `tools: yes|none|unknown`
  per model in `/v1/models`.
- `sse_wrap` try/finally guarantees `data: [DONE]` even when upstream truncates — truncated
  streams otherwise hang the browser reader loop forever.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
