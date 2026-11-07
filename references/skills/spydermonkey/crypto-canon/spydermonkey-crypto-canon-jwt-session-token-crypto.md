# JWT & session-token crypto

- source canon: `spydermonkey/crypto-canon.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-07

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| alg=none | `jwt_tool -M none` on OWN issued token | none accepted |
| HS/RS confusion | `jwt_tool -X k` (own public key as HMAC) | signature verified with pubkey bytes |
| Weak HMAC | `hashcat -m 16500` on own token | secret cracked |
| kid/path trick | `jwt_tool` kid traversal (own token) | file-read marker |
| jku/x5u open | `jwt_tool -M pb` (own token) | attacker-supplied JWKS accepted (lab) |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
