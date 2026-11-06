# Backup extraction and root-detection gaps — iot / machine

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-backup-extraction-and-root-de.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **iot** · auth **machine** · chain role **entry**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

allowBackup=true and client-only root/jail checks. Decisive test: adb backup pull of your build; the bypass shim on your device — the class is the check's client-side placement.

## Probe adjustment (iot × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
