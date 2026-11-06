# Fleet probe results (38 public models, 2026-10-06) — grpc / unauth

- source canon: `holyshit-mode/case-obsidian-y-api-reengage5-provider-wiring.md`
- base technique: `holyshit-mode-case-obsidian-y-api-reengage5-provider-wiring-.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **grpc** · auth **unauth** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- 30/38 LIVE; dead: `asdisunknown/*` (3), `tencent/hy3`, `xiaomi/mimo-v2.5`, `ollama/llama4`,
  `ollama/qwen3.6-35b` (timeout).
- **NATIVE tool-calling on 27 of 30 live models** — big change vs 2026-10-05 when upstream
  ignored `tools`. hyb/* fleet, ling, laguna, muse, ollama gemma/qwen all emit real
  `tool_calls`. ONLY `meituan/longcat-2.0` ignores tools. → tool support on LLM gateways is
  PER-UPSTREAM-MODEL and CHANGES between sessions; probe every model with a real tool def +
  tool-needing prompt, don't assume.

## Probe adjustment (grpc × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
