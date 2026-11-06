# 1. Supply-chain orchestration leak — `GET /status?json=1` (score 60-70) — android / machine

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-1-supply-chain-o.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **android** · auth **machine** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (android × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
