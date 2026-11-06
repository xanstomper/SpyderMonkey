# Hermes fallback debugging (user-reported "keeps falling back / some models not working") — chain composition

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-gateway-mint.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-gateway-mint-hermes-f.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Two independent causes, both diagnosed in one pass:
1. **`fallback_model` chain pointed at dead providers** (obsidian-free models + freeinference).
   Any transient freeforge error (429 throttle) silently "recovered" onto broken endpoints.
   Fix: replace chain with same-provider fallbacks (`freeforge/instant`, then
   `freeforge/deepseek-v4-pro`) so retries stay in-family. Verify with
   `hermes_cli.fallback_config.get_fallback_chain(yaml.safe_load(config))` — note
   `fallback_providers` key takes priority over `fallback_model` if both exist.
2. **Stale master key in `~/.hermes/.env`** — the key printed at server startup came from an
   older DB generation; the running server's `freeforge.db` (`meta` table, `master` row) holds
   the real one. Symptom: direct curl 200 but hermes 401 → 401s trigger fallback churn.
   Fix: read master from the SQLite DB, sed it into `.env`.
   Rule: **read the authoritative key from the server's DB, not from startup logs**, and diff
   `.env` value vs DB before debugging anything else in provider wiring.
- "Some models don't work" can also just be the shared per-IP 20/min throttle queueing a model
  (~90s+ for one call after a burst) — retest alone with a longer timeout before treating it
  as dead. grok-4-6 behaved exactly this way and passed on solo retest.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
