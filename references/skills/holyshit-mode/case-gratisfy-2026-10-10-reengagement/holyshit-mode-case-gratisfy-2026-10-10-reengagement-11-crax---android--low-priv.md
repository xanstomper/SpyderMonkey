# 11. crax-gpt catalog unlocked via gxyz key (11/17 models live-fire 200) — android / low-priv

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-reengagement-11-crax-.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **android** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

claude-opus-5, gpt-6-astra, grok-4-6, deepseek-v4-pro, kimi-k3, gpt-5-6-sol, gpt-5-5, claude-sonnet-5, claude-fable-5-1, gemini-3-8-flash, instant. **NATIVE tool calling verified on opus-5** (real `tool_calls` + `finish_reason:tool_calls`, no shim needed). Coding verified on deepseek-v4-pro. Dead: glm-5.3/5.3-flash (Z.ai USER_BLOCKED upstream), kimi-k2-6 (blank). **Streaming broken provider-side** ("Upstream returned invalid JSON payload" — their bug; non-streaming fine). Rate limit 5 req/10s + 20 req/60s **per IP** — account rotation does NOT help; sleep 13–15s between calls.

## Probe adjustment (android × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
