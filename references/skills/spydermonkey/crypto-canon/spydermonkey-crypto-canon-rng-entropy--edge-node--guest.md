# RNG & entropy — edge-node / guest

- source canon: `spydermonkey/crypto-canon.md`
- base technique: `spydermonkey-crypto-canon-rng-entropy.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **edge-node** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Predictable tokens | collect own session tokens, `ent` analysis | low entropy / sequential |
| Kernel entropy | `cat /proc/sys/kernel/random/entropy_avail` (own host) | critically low |
| rand() seeds | `crackle`-class on own BLE pairing frames (own device) | predictable MIC |

Walls: hash/token/key material is the OPERATOR'S OWN (dumps from own estate,
tokens issued to the operator, keys the operator holds). Cracking runs only
against own material. No ciphertext the operator does not legitimately hold.

## Probe adjustment (edge-node × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
