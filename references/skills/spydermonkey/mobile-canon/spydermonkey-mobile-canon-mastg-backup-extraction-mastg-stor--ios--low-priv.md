# MASTG Backup Extraction (MASTG-STORAGE-06) — ios / low-priv

- source canon: `spydermonkey/mobile-canon.md`
- base technique: `spydermonkey-mobile-canon-mastg-backup-extraction-mastg-stor.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **ios** · auth **low-priv** · chain role **entry**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- class: adb backup / iOS backup exposing app data
- probe: lab backup of the lab app; inventory the extracted class
- wall: lab only

## Probe adjustment (ios × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
