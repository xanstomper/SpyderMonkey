# WSTG-ATHN-05 Logout and Browser Cache

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: session data alive in browser cache after logout
- probe: cache-control header inventory on the lab replica's authed pages
- wall: read-only headers

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
