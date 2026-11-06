# 4. Verifying an exposed archive before declaring a DB leak — edge / machine

- source canon: `holyshit-mode/control-escalation-negatives.md`
- base technique: `holyshit-mode-control-escalation-negatives-4-verifying-an-ex.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **edge** · auth **machine** · chain role **pivot**

## Context

- platform: rate/segmentation differences — masscan-class first, then the app layer
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Download a candidate backup with a Range header first (`Range: bytes=0-200`), check the magic
(`PK` = zip), then pull full bytes and list `zipfile.namelist()` + `getinfo().file_size`. A `.zip`
whose members are all `.jpg`/media is a photo archive, not a credentials dump. Don't report "DB
backup exposed" from the filename alone.

## Probe adjustment (edge × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
