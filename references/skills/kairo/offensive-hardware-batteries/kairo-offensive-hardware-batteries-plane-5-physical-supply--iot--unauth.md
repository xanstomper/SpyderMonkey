# Plane 5 — Physical & supply — iot / unauth

- source canon: `kairo/offensive-hardware-batteries.md`
- base technique: `kairo-offensive-hardware-batteries-plane-5-physical-supply.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **iot** · auth **unauth** · chain role **pivot**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Tamper/documentation | visual + silkscreen review (no opening if not owned) | exposed debug headers, test points |
| Default credentials | documented vendor default lists vs device login (declared estate) | login with default |
| OEM/ODM surface | firmware strings/manufacturer portal enumeration (public) | OEM image/backdoor suspicion documented |
| Implant analysis | on OWN device: PCB review, unknown-component identification | unexpected modem/crypto/logging IC |
| Supply-chain image | hash + sign comparison of shipped image vs vendor published (owned) | image mismatch |

## Probe adjustment (iot × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
