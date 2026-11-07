# Discovery layer (authorized/bfe)

- source canon: `spydermonkey/osint-deep-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| BreachCLI | `pwned`-style check on own corpus | leaked accounts |
| Credential stuffing Feasibility | count of unique creds in OWN corpus | reaching attack material |
| Suppliers chain | public vendor docs (in scope) | third-party attack surface |
| Social graph | `maigret` mutuals (public) | trusted-personas map |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
