# Discovery System Network Connections (T1049) — dns / unauth

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-discovery-system-network-connectio.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- context: **dns** · auth **unauth** · chain role **pivot**

## Context

- platform: record/cname surface — the domtake chain starts here
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: connection/route enumeration
- probe: passive — headers/proxies reveal topology without touching hosts
- wall: NO-GAIN

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
