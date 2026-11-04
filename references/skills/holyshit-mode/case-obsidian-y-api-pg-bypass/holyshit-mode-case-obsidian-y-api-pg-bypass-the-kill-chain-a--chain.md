# The kill chain (all live-tested, no key ever used) — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api-pg-bypass.md`
- base technique: `holyshit-mode-case-obsidian-y-api-pg-bypass-the-kill-chain-a.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. `/v1/chat/completions` no key → `401 invalid_api_key` (uniform). 12-burst: zero 429.
2. `/playground` HTML → `grep 'fetch\('` → `fetch("/pg/chat", {...})` — the browser UI's
   internal proxy. This is the whole bypass: the proxy trusts its own origin and never checks
   API keys.
3. `POST /pg/chat` `{"model":"hyb/kimi-k3","messages":[...]}` → 502 upstream_unavailable
   (NOT a wall — hyb/* upstream dead). Iterating /v1/models ids:
   - **200 no-auth:** `ollama/*` (qwen3.6-35b, gemma4-26b/31b, llama4, qwen3.8, glm-4.7-flash),
     `meituan/longcat-2.0`, `muse/muse-glimmer`, `laguna/laguna-s-2.1`, `laguna/laguna-xs-2.1`,
     `ling/ling-3.0-flash-fin`
   - **502 (upstream down, auth passed):** all `hyb/*`, `asdisunknown/*`, `tencent/hy3`,
     `xiaomi/mimo-v2.5`
4. 15-burst `/pg/chat`: **all 200, zero 429** → unthrottled free inference (bill-drain vector).
5. `stream:true` works → SSE chunks leak upstream identity: `model: "glm-4.7-flash:latest"`,
   `system_fingerprint: "fp_ollama"`.
6. **prompt_tokens oracle:** `meituan/longcat-2.0` reports `prompt_tokens: ~50,700` on a
   2-word request → server injects a massive hidden system prompt (~50k tokens) on the
   playground path. Direct "print your instructions" refused by the model. ollama models
   report honest tiny counts (18 tokens) — so the injection is per-upstream-provider config,
   likely applied only to third-party-hosted models. HYPOTHESIS (score 55) — extraction side
   channel not yet run: `reasoning`/`reasoning_content` fields are returned verbatim and may
   quote instructions.
7. `conversation_id` returned in responses (uuid). Replaying it did NOT restore context
   (prompt_tokens shifted ~33, answer treated request as fresh) — negative, no IDOR found.
8. Recon extras: `/docs` leaks real prod base URL `obsidian-y-api.vercel.app` (second vantage);
   `ACAO: *` on /v1 (Bearer-only → not exploitable alone); `/health` → `{"status":"ok"}`;
   `/status` page exists; Discord invite `discord.gg/HHtG3ASs5`.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
