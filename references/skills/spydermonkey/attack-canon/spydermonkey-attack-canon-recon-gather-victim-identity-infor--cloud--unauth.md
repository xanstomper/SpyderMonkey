# Recon Gather Victim Identity Information (T1589) — cloud / unauth

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-recon-gather-victim-identity-infor.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **cloud** · auth **unauth** · chain role **entry**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: email formats, employee names, SSO portals, password policies visible pre-auth
- probe: harvest from public pages + error strings; enumerate the auth surface's hints
- wall: passive-first; no account interaction beyond what scope declares

## Probe adjustment (cloud × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
