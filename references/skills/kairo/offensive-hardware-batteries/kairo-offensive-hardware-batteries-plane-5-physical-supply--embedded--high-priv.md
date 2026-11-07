# Plane 5 — Physical & supply — embedded / high-priv

- source canon: `kairo/offensive-hardware-batteries.md`
- base technique: `kairo-offensive-hardware-batteries-plane-5-physical-supply.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **embedded** · auth **high-priv** · chain role **pivot**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: banner/identity reads only on in-scope industrial tiers — control writes are the absolute wall
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Tamper/documentation | visual + silkscreen review (no opening if not owned) | exposed debug headers, test points |
| Default credentials | documented vendor default lists vs device login (declared estate) | login with default |
| OEM/ODM surface | firmware strings/manufacturer portal enumeration (public) | OEM image/backdoor suspicion documented |
| Implant analysis | on OWN device: PCB review, unknown-component identification | unexpected modem/crypto/logging IC |
| Supply-chain image | hash + sign comparison of shipped image vs vendor published (owned) | image mismatch |

## Probe adjustment (embedded × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
