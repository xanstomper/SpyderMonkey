# 10.4 Reasoning/CoT + prompt extraction (score 85) — grpc / high-priv

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- base technique: `3am-shinjitsu-arsenal-10-llm-ai-10-4-reasoning-cot-prompt-ex.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **grpc** · auth **high-priv** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- `reasoning_content` field = the extraction side-channel (structurally distinct field the
  client renders). Hidden-prompt-size fingerprint: minimal completions → constant huge
  `prompt_tokens` = server-injected system prompt; structural section queries extract it
  when direct reads are refused (temp-0, one axis per question).

## Probe adjustment (grpc × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
