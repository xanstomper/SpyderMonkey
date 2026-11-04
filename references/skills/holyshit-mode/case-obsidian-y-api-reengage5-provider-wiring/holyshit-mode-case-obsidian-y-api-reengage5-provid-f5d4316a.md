# Fleet probe results (38 public models, 2026-10-06)

- source canon: `holyshit-mode/case-obsidian-y-api-reengage5-provider-wiring.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

- 30/38 LIVE; dead: `asdisunknown/*` (3), `tencent/hy3`, `xiaomi/mimo-v2.5`, `ollama/llama4`,
  `ollama/qwen3.6-35b` (timeout).
- **NATIVE tool-calling on 27 of 30 live models** — big change vs 2026-10-05 when upstream
  ignored `tools`. hyb/* fleet, ling, laguna, muse, ollama gemma/qwen all emit real
  `tool_calls`. ONLY `meituan/longcat-2.0` ignores tools. → tool support on LLM gateways is
  PER-UPSTREAM-MODEL and CHANGES between sessions; probe every model with a real tool def +
  tool-needing prompt, don't assume.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
