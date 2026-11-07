# Credential Access Credentials from Password Stores (T1555)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **PTES-PE** · **CWE-522** · **ATT&CK T1555**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: browser/keychain credential extraction
- probe: REFUSED on any live endpoint; the class exists as a detection pattern
- wall: kage rule only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
