# Backup extraction and root-detection gaps — android / unauth

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-backup-extraction-and-root-de.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **android** · auth **unauth** · chain role **entry**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

allowBackup=true and client-only root/jail checks. Decisive test: adb backup pull of your build; the bypass shim on your device — the class is the check's client-side placement.

## Probe adjustment (android × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
