# Resource Development Obtain Capabilities (T1588)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: acquiring existing tooling
- probe: inventory what the operator environment already carries (arsenal.py)
- wall: zero-purchase; the arsenal maps presence, never installs for an engagement

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
