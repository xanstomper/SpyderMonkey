# Recon Search Closed Sources (T1597) — host / unauth

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-recon-search-closed-sources-t1597.md`
- bindings: **PTES-PE** · **CWE-522** · **ATT&CK T1555**
- context: **host** · auth **unauth** · chain role **entry**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: paid/registered intel sources for victim data
- probe: only what the operator legally holds credentials for
- wall: no credential use beyond declared scope; nothing purchased mid-run

## Probe adjustment (host × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
