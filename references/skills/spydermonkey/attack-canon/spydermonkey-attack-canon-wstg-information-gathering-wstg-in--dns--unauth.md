# WSTG Information Gathering (WSTG-INFO) — dns / unauth

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-wstg-information-gathering-wstg-in.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **dns** · auth **unauth** · chain role **entry**

## Context

- platform: record/cname surface — the domtake chain starts here
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: fingerprinting, disclosure, open ports, error pages
- probe: banner/error/source-map/harvest classes — all read-only
- wall: ledger every source with provenance

## Probe adjustment (dns × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
