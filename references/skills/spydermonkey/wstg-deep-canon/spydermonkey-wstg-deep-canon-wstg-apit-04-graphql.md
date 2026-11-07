# WSTG-APIT-04 GraphQL

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: introspection open, field-level authz gaps, batching abuse
- probe: introspection query + aliased duplicate fields on the lab endpoint
- wall: lab replica

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
