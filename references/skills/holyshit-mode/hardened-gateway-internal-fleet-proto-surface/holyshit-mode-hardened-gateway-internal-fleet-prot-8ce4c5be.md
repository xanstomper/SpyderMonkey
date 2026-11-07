# When to use

- source canon: `holyshit-mode/hardened-gateway-internal-fleet-proto-surface.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

A public OpenAI-compatible gateway / LLM platform is **professionally hardened** — every `/v1/*` and
`/api/*` route keyed, Turnstile on all bootstrap, opaque DB sessions, no JWT in bundles, no IDOR on the
pre-auth management API. The compromisable surface then often lives on the operator's **internal
serving fleet**, reachable because (a) it is publicly IP-addressed and (b) a worker-level proto surface
was left unauthenticated while the public edge is keyed.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
