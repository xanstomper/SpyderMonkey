# U14 Detection & response — container / low-priv

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u14-detection-response.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **container** · auth **low-priv** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- [ ] Asset coverage mapped against SIEM/EDR/NDR data sources
- [ ] High-value alerts tested through approved purple-team cases
- [ ] Log integrity, time sync, retention, and forensic readiness verified
- [ ] Incident runbooks, revocation, and rollback paths exercised
- [ ] Detection gaps and tuning backlog documented

## Probe adjustment (container × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
