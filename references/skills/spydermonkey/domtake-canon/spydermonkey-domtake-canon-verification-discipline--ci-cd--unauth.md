# Verification discipline — ci-cd / unauth

- source canon: `spydermonkey/domtake-canon.md`
- base technique: `spydermonkey-domtake-canon-verification-discipline.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **ci-cd** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

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

## Probe adjustment (ci-cd × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
