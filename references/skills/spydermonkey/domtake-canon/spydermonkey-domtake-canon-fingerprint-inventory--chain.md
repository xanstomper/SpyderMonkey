# Fingerprint inventory — chain composition

- source canon: `spydermonkey/domtake-canon.md`
- base technique: `spydermonkey-domtake-canon-fingerprint-inventory.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Probe | Test | Confirmed-when |
|---|---|---|
| CNAME map | `dnsx -cname` (own domains) | cname rows collected |
| Provider check | `can-i-take-over-xyz` lookup on cname target | provider in takeover table |
| Status code | `httpx -sc` on the host | 404/NoSuchBucket signatures |
| Edge cert | `tlsx -san -cn` on the host | cert for dead service |
| NS delegation | `dig NS` on dangling sub (own) | delegated but dead |
| Mail takeover | `dig MX` on sub (own) | mx name claimable |
| Service tick | probe service endpoint (own sub) | claimable marker |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
