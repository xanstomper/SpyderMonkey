# Known-key & entity attacks (own keys) — iot-edge / service

- source canon: `spydermonkey/crypto-canon.md`
- base technique: `spydermonkey-crypto-canon-known-key-entity-attacks-own-keys.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **iot-edge** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Default/root CAs | `openssl verify -CAfile` chain trace (own infra) | private CA in device trust store |
| Key reuse | `rsactftool` / `openssl` modulus gcd across own keys | shared modulus / reused p,q |
| Weak exponents | `openssl rsa -text` on own key | e=3 / small d |
| Cert pasting | `certigo` own-host chain dump | mismatched SAN/CN for the name |

## Probe adjustment (iot-edge × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
