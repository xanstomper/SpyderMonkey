# HOLY SHIT #1 — Unauthenticated free AI via playground proxy (score 90) — iot / high-priv

- source canon: `holyshit-mode/case-obsidian-y-api.md`
- base technique: `holyshit-mode-case-obsidian-y-api-holy-shit-1-unauthenticate.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iot** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

`POST /pg/chat` — the playground's internal backend path — requires NO API key and serves real completions. The operator assumed /pg/* was internal; it's internet-reachable.
- Working models at test time: `meituan/longcat-2.0`, `ollama/*` (qwen3.6-35b, gemma4-26b, llama4, qwen3.8), `muse/muse-glimmer`, `laguna/*`, `ling/ling-3.0-flash-fin`. `hyb/*`+`asdisunknown/*` upstream 502 (down at test time, same free access).
- Malformed requests give clean validation errors (`messages must be a non-empty list`) — fine-grained oracle, model existence via `model_not_found` vs 502.
- Same vuln on the Vercel host — always test BOTH hosts when docs leak a second base URL (docs page contained the vercel URL verbatim).
- 15-burst: zero 429s. No rate limiter anywhere.

## Probe adjustment (iot × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
