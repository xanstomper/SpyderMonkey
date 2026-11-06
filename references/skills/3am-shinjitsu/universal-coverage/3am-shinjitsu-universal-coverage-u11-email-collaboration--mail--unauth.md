# U11 Email & collaboration — mail / unauth

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u11-email-collaboration.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- context: **mail** · auth **unauth** · chain role **pivot**

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- [ ] MX/SPF/DKIM/DMARC/MTA-STS/TLS-RPT checked and aligned
- [ ] Mailbox/SaaS sharing links, external guests, helpdesk/reset trust reviewed
- [ ] Anti-phishing controls and reporting paths validated (documentation only unless RoE)
- [ ] Domain spoofing/lookalike domains and tenant takeover risks documented
- [ ] Audit logs and retention for collaboration platforms reviewed

## Probe adjustment (mail × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
