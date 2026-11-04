# 7.5 Registry/CI secret exposure (score 85 when found) — graphql / unauth

- source canon: `3am-shinjitsu/arsenal-07-supply-chain.md`
- base technique: `3am-shinjitsu-arsenal-07-supply-chain-7-5-registry-ci-secret.md`
- bindings: **WSTG-SESS-01** · **CWE-347** · **ATT&CK T1552**
- context: **graphql** · auth **unauth** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Public repo/paste scan of org namespace for keys (`sk_`, `eyJ` JWT shapes, `AKIA`),
  workflow logs, committed `.env` history (git log on public clones).
- A leaked key = a FINDING, not a license: one read-only privilege confirmation (`/v1/credits`
  class balance endpoint), then documentation (§2 scope gate).

## Probe adjustment (graphql × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
