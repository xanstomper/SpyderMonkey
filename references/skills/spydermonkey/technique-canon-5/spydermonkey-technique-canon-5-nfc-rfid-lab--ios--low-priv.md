# NFC/RFID (lab) — ios / low-priv

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-nfc-rfid-lab.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **ios** · auth **low-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

UID-tag reads on lab badges — the readable-UID class (static-UID tags = cloneable-class, documented). Decisive test: your own lab badge read twice — identical UID = the class row.

## Probe adjustment (ios × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
