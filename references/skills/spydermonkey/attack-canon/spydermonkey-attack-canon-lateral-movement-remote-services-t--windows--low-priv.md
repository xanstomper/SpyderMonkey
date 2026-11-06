# Lateral Movement Remote Services (T1021) — windows / low-priv

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-lateral-movement-remote-services-t.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **windows** · auth **low-priv** · chain role **pivot**

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- class: ssh/smb/winrm hopping
- probe: never fired — the AUTHZ ladder CROWNS the reachability, stops there
- wall: NO-GAIN; lateral movement execution is refused

## Probe adjustment (windows × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
