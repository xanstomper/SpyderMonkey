# 4. CONFIRMED — Internal gateways expose full API specs publicly (score 50) — websocket / low-priv

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-4-confirmed-internal-.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **websocket** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- `GET https://wm.xplabs.ai/openapi.json` → 200 (242KB, full vLLM/OpenAI/Anthropic surface +
  control-plane routes: `/scale_elastic_ep`, `/is_scaling_elastic_ep`, `/kv_event_sources`,
  `/generative_scoring`, `/tokenize`, `/load`, `/measure`).
- `GET https://gateway.xplabs.ai/openapi.json` and `/docs` → 200.
- **IMPACT:** Full internal surface map + control-plane discovery primitive. This is what
  made Finding 1 trivially discoverable.

## Probe adjustment (websocket × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
