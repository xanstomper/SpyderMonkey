# Hermes integration (verified live) — chain composition

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-gateway-mint.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-gateway-mint-hermes-i.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
