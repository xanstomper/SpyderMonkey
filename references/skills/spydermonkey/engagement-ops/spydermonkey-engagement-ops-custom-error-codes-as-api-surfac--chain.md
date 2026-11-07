# Custom error codes as API surface signals — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-custom-error-codes-as-api-surfac.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

A custom error code (e.g. HTTP 200 or 404 with JSON body: `code:1901, msg:"Oops, coco is gone!", data:{}`) is NOT a standard 404 — it means the route EXISTS on the server but is returning a specific application-level error instead of a generic HTTP code. This pattern reveals:

1. **Hidden API surface**: Every endpoint that returns a custom error code is a route that SHOULD exist, revealing the API design without requiring authentication.
2. **Error taxonomy**: The error code itself (1901 vs 4001 vs 6002) can be used for API fingerprinting and distinguishing between "route exists but needs auth" vs "route doesn't exist" vs "route exists but method wrong" (405).
3. **Intelligence value**: Capture the full error response in ledger findings. The error code is itself a finding — it reveals the API gateway's auth-swallow behavior.

Always differentiate: standard 404 (route doesn't exist) vs custom error code (route exists, gateway swallowing auth). The latter is a ledger-worthy finding.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
