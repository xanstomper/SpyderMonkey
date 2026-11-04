# 10.4 Reasoning/CoT + prompt extraction (score 85)

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## The technique

- `reasoning_content` field = the extraction side-channel (structurally distinct field the
  client renders). Hidden-prompt-size fingerprint: minimal completions → constant huge
  `prompt_tokens` = server-injected system prompt; structural section queries extract it
  when direct reads are refused (temp-0, one axis per question).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
