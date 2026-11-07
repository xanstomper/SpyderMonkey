# Lateral Movement Remote Services (T1021) — macos / root

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-lateral-movement-remote-services-t.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **macos** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: darwin surface — read-only inventory first; the documented class applies to the same daemon/services layer
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- class: ssh/smb/winrm hopping
- probe: never fired — the AUTHZ ladder CROWNS the reachability, stops there
- wall: NO-GAIN; lateral movement execution is refused

## Probe adjustment (macos × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
