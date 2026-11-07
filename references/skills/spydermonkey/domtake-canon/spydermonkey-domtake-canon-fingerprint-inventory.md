# Fingerprint inventory

- source canon: `spydermonkey/domtake-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| CNAME map | `dnsx -cname` (own domains) | cname rows collected |
| Provider check | `can-i-take-over-xyz` lookup on cname target | provider in takeover table |
| Status code | `httpx -sc` on the host | 404/NoSuchBucket signatures |
| Edge cert | `tlsx -san -cn` on the host | cert for dead service |
| NS delegation | `dig NS` on dangling sub (own) | delegated but dead |
| Mail takeover | `dig MX` on sub (own) | mx name claimable |
| Service tick | probe service endpoint (own sub) | claimable marker |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
