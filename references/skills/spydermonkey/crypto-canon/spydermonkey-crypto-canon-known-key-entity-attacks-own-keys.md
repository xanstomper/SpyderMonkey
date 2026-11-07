# Known-key & entity attacks (own keys)

- source canon: `spydermonkey/crypto-canon.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Default/root CAs | `openssl verify -CAfile` chain trace (own infra) | private CA in device trust store |
| Key reuse | `rsactftool` / `openssl` modulus gcd across own keys | shared modulus / reused p,q |
| Weak exponents | `openssl rsa -text` on own key | e=3 / small d |
| Cert pasting | `certigo` own-host chain dump | mismatched SAN/CN for the name |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
