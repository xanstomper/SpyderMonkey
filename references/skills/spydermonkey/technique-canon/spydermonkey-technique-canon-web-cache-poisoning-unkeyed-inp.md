# Web cache poisoning (unkeyed input reflect)

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Unkeyed header values cached into the response. Decisive test: header X with a unique marker, then a second unauthenticated request returning the marker = poisoned (one cache entry, your own marker, never a real user's path).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
