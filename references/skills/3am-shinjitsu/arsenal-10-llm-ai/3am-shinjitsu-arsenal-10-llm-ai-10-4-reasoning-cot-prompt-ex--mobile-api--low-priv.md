# 10.4 Reasoning/CoT + prompt extraction (score 85) — mobile-api / low-priv

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- base technique: `3am-shinjitsu-arsenal-10-llm-ai-10-4-reasoning-cot-prompt-ex.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **mobile-api** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- `reasoning_content` field = the extraction side-channel (structurally distinct field the
  client renders). Hidden-prompt-size fingerprint: minimal completions → constant huge
  `prompt_tokens` = server-injected system prompt; structural section queries extract it
  when direct reads are refused (temp-0, one axis per question).

## Probe adjustment (mobile-api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
