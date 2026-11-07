# Hermes fallback debugging (user-reported "keeps falling back / some models not working")

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-gateway-mint.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
