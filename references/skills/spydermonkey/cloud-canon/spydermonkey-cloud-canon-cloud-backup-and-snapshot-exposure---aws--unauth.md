# Cloud Backup and Snapshot Exposure (CLOUD-OBJ-03) — aws / unauth

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-backup-and-snapshot-exposure-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **aws** · auth **unauth** · chain role **entry**

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: public/shared snapshots — the volume class
- probe: read-only snapshot attribute inventory of the declared estate
- wall: values never restored; exposure crowned only

## Probe adjustment (aws × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
