# Command and Control Proxy (T1090) — dns / unauth

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-command-and-control-proxy-t1090.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- context: **dns** · auth **unauth** · chain role **pivot**

## Context

- platform: record/cname surface — the domtake chain starts here
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: tunneling through proxies
- probe: the family maps proxy headers (x-forwarded chains) as inventory only
- wall: read-only

## Probe adjustment (dns × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
