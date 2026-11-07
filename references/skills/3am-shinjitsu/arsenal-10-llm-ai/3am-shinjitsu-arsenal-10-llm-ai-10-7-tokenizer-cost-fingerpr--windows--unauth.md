# 10.7 Tokenizer/cost fingerprint (score 60) — windows / unauth

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- base technique: `3am-shinjitsu-arsenal-10-llm-ai-10-7-tokenizer-cost-fingerpr.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **windows** · auth **unauth** · chain role **entry**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Same prompt across "premium" tiers: identical token counts + identical completions at
  temp-0 = router placebo (cheap model behind premium label). Capability SVG test + temp-0
  open-ended diversity for the model-behind-the-label map.

## Probe adjustment (windows × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
