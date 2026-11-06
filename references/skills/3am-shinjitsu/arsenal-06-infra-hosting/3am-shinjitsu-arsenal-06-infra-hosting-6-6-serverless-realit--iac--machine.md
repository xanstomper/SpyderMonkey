# 6.6 Serverless reality check (score 30 → pivot immediately) — iac / machine

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- base technique: `3am-shinjitsu-arsenal-06-infra-hosting-6-6-serverless-realit.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **iac** · auth **machine** · chain role **pivot**

## Context

- platform: template/state files are the infrastructure inventory — read-only crown of the exposure
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- No filesystem, no process, no persistence surface = state it ONCE in the ledger and pivot
  to event/state planes: Workers KV/D1/R2 via misrouted routes, Lambda env-var secrets via
  error pages, queue poison-pill classes (read-only), durable-object cross-tenant id prediction.

## Probe adjustment (iac × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
