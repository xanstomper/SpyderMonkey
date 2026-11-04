# Discovery System Information Discovery (T1082) — edge / low-priv

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-discovery-system-information-disco.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- context: **edge** · auth **low-priv** · chain role **entry**

## Context

- platform: rate/segmentation differences — masscan-class first, then the app layer
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- class: OS/build/hostname enumeration
- probe: banner + header differentials; error-page fingerprinting
- wall: read-only

## Probe adjustment (edge × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
