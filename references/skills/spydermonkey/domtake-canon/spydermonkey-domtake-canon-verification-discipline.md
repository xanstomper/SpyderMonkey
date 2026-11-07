# Verification discipline

- source canon: `spydermonkey/domtake-canon.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Scope gate | `scope check` on every candidate fqdn | in estate |
| No registration | candidate recorded, NEVER registered (unless disclosed) | ledger row, no claim |
| Owner contact | `whois` owner == operator/estate | ownership confirmed |
| Disclosure path | engagement report row for each candidate | documented |

Walls: a confirmed claimable subdomain is a FINDING, not a prize: the family
registers nothing on third-party names without written authorization —
verification is a fingerprint + ledger row, never an actual takeover of a
domain outside the engagement.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
