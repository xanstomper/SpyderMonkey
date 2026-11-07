# Verification discipline — chain composition

- source canon: `spydermonkey/domtake-canon.md`
- base technique: `spydermonkey-domtake-canon-verification-discipline.md`
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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
