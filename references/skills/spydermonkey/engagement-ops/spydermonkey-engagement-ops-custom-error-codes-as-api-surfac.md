# Custom error codes as API surface signals

- source canon: `spydermonkey/engagement-ops.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

A custom error code (e.g. HTTP 200 or 404 with JSON body: `code:1901, msg:"Oops, coco is gone!", data:{}`) is NOT a standard 404 — it means the route EXISTS on the server but is returning a specific application-level error instead of a generic HTTP code. This pattern reveals:

1. **Hidden API surface**: Every endpoint that returns a custom error code is a route that SHOULD exist, revealing the API design without requiring authentication.
2. **Error taxonomy**: The error code itself (1901 vs 4001 vs 6002) can be used for API fingerprinting and distinguishing between "route exists but needs auth" vs "route doesn't exist" vs "route exists but method wrong" (405).
3. **Intelligence value**: Capture the full error response in ledger findings. The error code is itself a finding — it reveals the API gateway's auth-swallow behavior.

Always differentiate: standard 404 (route doesn't exist) vs custom error code (route exists, gateway swallowing auth). The latter is a ledger-worthy finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
