# Kill-chain

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Recon (keyless catalog + SPF + DNS) → internal-fleet enumeration (`*.xplabs.ai` base_url leak
in `/api/models`) → internal control-plane discovery (`/openapi.json`) → **unauth free-AI
inference (`/invocations`, premium models) + unauth elastic-scaling control-plane
(`/scale_elastic_ep`) = Impact**.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
