# 11. crax-gpt catalog unlocked via gxyz key (11/17 models live-fire 200)

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- generated: 2026-11-04

## The technique

claude-opus-5, gpt-6-astra, grok-4-6, deepseek-v4-pro, kimi-k3, gpt-5-6-sol, gpt-5-5, claude-sonnet-5, claude-fable-5-1, gemini-3-8-flash, instant. **NATIVE tool calling verified on opus-5** (real `tool_calls` + `finish_reason:tool_calls`, no shim needed). Coding verified on deepseek-v4-pro. Dead: glm-5.3/5.3-flash (Z.ai USER_BLOCKED upstream), kimi-k2-6 (blank). **Streaming broken provider-side** ("Upstream returned invalid JSON payload" — their bug; non-streaming fine). Rate limit 5 req/10s + 20 req/60s **per IP** — account rotation does NOT help; sleep 13–15s between calls.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
