# 1. Supply-chain orchestration leak — `GET /status?json=1` (score 60-70)

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Unauth status JSON dumps the ENTIRE upstream provider fleet:
- 10 aggregator providers: `deepseek, gonka, hyb, kallme, kiosapi, longcat, muse, ollama, stealth, yjs`
- Crypto-billing host: `gonka-api.org` ("balance too low, top up via crypto, no subscription")
- Router host: `router.kiosapi.com/v1/chat/completions` (kiosapi)
- Internal backend name: `hyb` calls its backend **"venesus"** (`venesus chat error 404` in bodies)
- Taiwanese `yjs` distributor, Chinese error with request IDs:
  `分組 auto 下模型 laguna-s-2.1 無可用管道（distributor） (request id: 202610061000176252022908268d9d6nWCOUkyz)`
  → reveals a "distributor" pipeline architecture under yjs.
- `stealth/ox-alpha` upstream returns raw legacy IE6-era HTML (different originating stack).
- `kallme/*` upstream = Anthropic chromium fleet (503s).
- 49 models total in status vs fewer in public `/v1/models` — extras are the hidden/provisioned tier.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
