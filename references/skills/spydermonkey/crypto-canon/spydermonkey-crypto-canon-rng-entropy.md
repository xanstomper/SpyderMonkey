# RNG & entropy

- source canon: `spydermonkey/crypto-canon.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Predictable tokens | collect own session tokens, `ent` analysis | low entropy / sequential |
| Kernel entropy | `cat /proc/sys/kernel/random/entropy_avail` (own host) | critically low |
| rand() seeds | `crackle`-class on own BLE pairing frames (own device) | predictable MIC |

Walls: hash/token/key material is the OPERATOR'S OWN (dumps from own estate,
tokens issued to the operator, keys the operator holds). Cracking runs only
against own material. No ciphertext the operator does not legitimately hold.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
