# RNG & entropy — browser / machine

- source canon: `spydermonkey/crypto-canon.md`
- base technique: `spydermonkey-crypto-canon-rng-entropy.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **browser** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Predictable tokens | collect own session tokens, `ent` analysis | low entropy / sequential |
| Kernel entropy | `cat /proc/sys/kernel/random/entropy_avail` (own host) | critically low |
| rand() seeds | `crackle`-class on own BLE pairing frames (own device) | predictable MIC |

Walls: hash/token/key material is the OPERATOR'S OWN (dumps from own estate,
tokens issued to the operator, keys the operator holds). Cracking runs only
against own material. No ciphertext the operator does not legitimately hold.

## Probe adjustment (browser × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
