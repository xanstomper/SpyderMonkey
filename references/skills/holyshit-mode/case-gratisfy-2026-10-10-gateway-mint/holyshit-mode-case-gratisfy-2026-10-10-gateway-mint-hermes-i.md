# Hermes integration (verified live)

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-gateway-mint.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-04

## The technique

- `~/.hermes/config.yaml` already had a `freeforge` custom provider (`base_url: localhost:8700/v1`,
  `key_env: FREEINFORGE_API_KEY`) but the `.env` key didn't match the server's master key —
  **check key-vs-server match before debugging routing**.
- Live-fire through hermes itself: gpt-6-astra executed a shell tool (2 calls, 3m);
  claude-opus-5 ran a full write→execute→verify loop (4 tool calls, 1m45s) producing a correct
  `/tmp/ff_prime.py`. Tool calling + looping + coding all work through the provider.
- Aux models (`auxiliary.title/vision`, `delegation.*`) set to freeforge ids so aux calls
  don't die on connection errors.
- hermes CLI gotcha: `hermes chat -q "…"` fails with "expected one argument" when the query
  contains shell-expansion chars; use `--query="…"` (=form) and single-quote.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
