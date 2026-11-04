# 10.2 PTOK drift oracle (score 90 — mandatory on every gateway re-entry) — websocket / unauth

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- base technique: `3am-shinjitsu-arsenal-10-llm-ai-10-2-ptok-drift-oracle-score.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **websocket** · auth **unauth** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- 3× identical minimal requests → `usage.prompt_tokens`: CONSTANT = stateless/patched;
  DRIFTING/GROWING = live cross-user server state (the shared global buffer).
- Drift confirmed → §10.4 poisoning becomes the WRITE primitive on that buffer (own gateway
  only; score 95 when cross-user verbatim recurrence is proven).

## Probe adjustment (websocket × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
