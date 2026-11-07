# Lateral Movement Remote Services (T1021)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: ssh/smb/winrm hopping
- probe: never fired — the AUTHZ ladder CROWNS the reachability, stops there
- wall: NO-GAIN; lateral movement execution is refused

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
