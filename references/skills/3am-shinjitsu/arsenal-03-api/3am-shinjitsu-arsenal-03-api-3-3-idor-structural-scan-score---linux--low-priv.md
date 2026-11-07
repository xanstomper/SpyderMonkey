# 3.3 IDOR structural scan (score 85) — linux / low-priv

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-3-idor-structural-scan-score-.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **linux** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- From §3.2 shapes: every cross-user identifier (`walletId`, `ownerId`, `userId`, `accountId`).
- DECISIVE: operator's own two accounts (or one ephemeral self-account) — swap ONLY the id,
  keep the valid session. Cross-account read/write = CONFIRMED.
- Numeric-id ladders on admin routes: `/users/1` `/grants/1` unauth + low-priv (GET then
  PATCH as own-id). All 401/403 uniform = negative.

## Probe adjustment (linux × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
