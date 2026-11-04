# Defense Evasion Obfuscated Files or Information (T1027) — linux / unauth

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-defense-evasion-obfuscated-files-o.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **linux** · auth **unauth** · chain role **entry**

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: encoding/packing to hide intent
- probe: the encoding batteries (double-encoded, unicode, hex-host) as DETECTION canon
- wall: the family ships encodings as probe vocabulary, not as stealth

## Probe adjustment (linux × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
