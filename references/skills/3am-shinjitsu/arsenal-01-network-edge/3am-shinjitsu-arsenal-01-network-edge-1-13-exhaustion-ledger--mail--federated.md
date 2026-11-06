# 1.13 Exhaustion ledger template (class 1) — mail / federated

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-13-exhaustion-ledger.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **mail** · auth **federated** · chain role **pivot**

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

```
{"class":"network/edge","probe":"3306-banner","test":"connect :3306 read greeting",
 "result":"5.5.5-10.1.48-MariaDB","verdict":"CONFIRMED","score":85,
 "next":"searchsploit mariadb 10.1 — documented PoC adaptation only"}

## Probe adjustment (mail × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
