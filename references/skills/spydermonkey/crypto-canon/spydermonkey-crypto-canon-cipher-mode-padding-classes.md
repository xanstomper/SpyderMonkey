# Cipher-mode & padding classes

- source canon: `spydermonkey/crypto-canon.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| ECB detect | duplicate ciphertext blocks on own oracle | ECB (blocks repeat) |
| CBC bitflip | flip own token byte, observe oracle | predictable plaintext change |
| IV reuse | capture two own sessions | identical IV across messages |
| Padding oracle (app) | `padbuster` on OWN app endpoint (lab) | oracle distinguishes padding |
| Nonce reuse | two own encryptions same nonce | keystream collision |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
