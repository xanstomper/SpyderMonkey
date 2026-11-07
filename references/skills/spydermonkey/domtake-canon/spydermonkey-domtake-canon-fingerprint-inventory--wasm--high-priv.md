# Fingerprint inventory — wasm / high-priv

- source canon: `spydermonkey/domtake-canon.md`
- base technique: `spydermonkey-domtake-canon-fingerprint-inventory.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **wasm** · auth **high-priv** · chain role **entry**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (wasm × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
