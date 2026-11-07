# HOLY SHIT #1 — Unauthenticated free AI via playground proxy (score 90)

- source canon: `holyshit-mode/case-obsidian-y-api.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`POST /pg/chat` — the playground's internal backend path — requires NO API key and serves real completions. The operator assumed /pg/* was internal; it's internet-reachable.
- Working models at test time: `meituan/longcat-2.0`, `ollama/*` (qwen3.6-35b, gemma4-26b, llama4, qwen3.8), `muse/muse-glimmer`, `laguna/*`, `ling/ling-3.0-flash-fin`. `hyb/*`+`asdisunknown/*` upstream 502 (down at test time, same free access).
- Malformed requests give clean validation errors (`messages must be a non-empty list`) — fine-grained oracle, model existence via `model_not_found` vs 502.
- Same vuln on the Vercel host — always test BOTH hosts when docs leak a second base URL (docs page contained the vercel URL verbatim).
- 15-burst: zero 429s. No rate limiter anywhere.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
