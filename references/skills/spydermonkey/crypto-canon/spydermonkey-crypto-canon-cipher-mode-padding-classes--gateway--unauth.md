# Cipher-mode & padding classes — gateway / unauth

- source canon: `spydermonkey/crypto-canon.md`
- base technique: `spydermonkey-crypto-canon-cipher-mode-padding-classes.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **gateway** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| ECB detect | duplicate ciphertext blocks on own oracle | ECB (blocks repeat) |
| CBC bitflip | flip own token byte, observe oracle | predictable plaintext change |
| IV reuse | capture two own sessions | identical IV across messages |
| Padding oracle (app) | `padbuster` on OWN app endpoint (lab) | oracle distinguishes padding |
| Nonce reuse | two own encryptions same nonce | keystream collision |

## Probe adjustment (gateway × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
