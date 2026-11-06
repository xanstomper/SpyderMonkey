# 10.8 Mint/signup chains (score 75) — kubernetes / machine

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- base technique: `3am-shinjitsu-arsenal-10-llm-ai-10-8-mint-signup-chains-scor.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **kubernetes** · auth **machine** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Free-tier automated signup → `sk_` key mint → `/v1/models` + `/v1/chat/completions` live +
  `/v1/credits` per-key `{usage, limit, balance}` leak (the only metadata endpoint). Signup
  on the TARGET with operator-authorized identities only (no third-party account fraud — §2).
- Reseller upstream = operator's supply-chain crown jewel: free-credit bleed on the reseller
  degrades the operator's own upstream — state the chain, never drain.

## Probe adjustment (kubernetes × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
