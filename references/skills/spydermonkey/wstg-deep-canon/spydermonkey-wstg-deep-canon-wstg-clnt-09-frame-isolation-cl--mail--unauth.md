# WSTG-CLNT-09 Frame Isolation (Clickjacking) — mail / unauth

- source canon: `spydermonkey/wstg-deep-canon.md`
- base technique: `spydermonkey-wstg-deep-canon-wstg-clnt-09-frame-isolation-cl.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **mail** · auth **unauth** · chain role **pivot**

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: missing X-Frame-Options/frame-ancestors
- probe: header inventory — the crown is the missing header, no live framing
- wall: read-only

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
