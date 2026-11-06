# Hermes integration (verified live) — container / unauth

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-gateway-mint.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-gateway-mint-hermes-i.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **container** · auth **unauth** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

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

## Probe adjustment (container × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
