# Cloud Backup and Snapshot Exposure (CLOUD-OBJ-03) — iac / high-priv

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-backup-and-snapshot-exposure-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **iac** · auth **high-priv** · chain role **entry**

## Context

- platform: template/state files are the infrastructure inventory — read-only crown of the exposure
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- class: public/shared snapshots — the volume class
- probe: read-only snapshot attribute inventory of the declared estate
- wall: values never restored; exposure crowned only

## Probe adjustment (iac × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
