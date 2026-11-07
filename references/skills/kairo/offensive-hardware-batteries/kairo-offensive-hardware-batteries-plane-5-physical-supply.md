# Plane 5 — Physical & supply

- source canon: `kairo/offensive-hardware-batteries.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Tamper/documentation | visual + silkscreen review (no opening if not owned) | exposed debug headers, test points |
| Default credentials | documented vendor default lists vs device login (declared estate) | login with default |
| OEM/ODM surface | firmware strings/manufacturer portal enumeration (public) | OEM image/backdoor suspicion documented |
| Implant analysis | on OWN device: PCB review, unknown-component identification | unexpected modem/crypto/logging IC |
| Supply-chain image | hash + sign comparison of shipped image vs vendor published (owned) | image mismatch |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
