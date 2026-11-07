# SPYDERMONKEY — Crypto Canon (v6.0)

Every cryptographic weakness class with its decisive read-only test. Own
keys, own tokens, own files only; NO-GAIN walls everywhere. Bindings: WSTG-CRYP · CWE-327/310/326 · ATT&CK T1640.

## Crypto inventory — what the estate uses

| Probe | Test | Confirmed-when |
|---|---|---|
| Cert inventory | `sslscan`/`testssl` + `openssl x509` on owned hosts | key size < 2048 / sha1 / expiring soon |
| Cipher survey | `testssl --cipher-per-proto` on own targets | RC4/3DES/null/anon suites present |
| Curve check | `openssl s_client -groups` on own host | secp256r1-only or weak curves |
| HSTS/forward secrecy | `tlsx -hsts` + key-exchange list | no PFS, no HSTS |
| Session resumption | `sslyze --resum` | ticket/no-resumption anomalies |

## Known-key & entity attacks (own keys)

| Probe | Test | Confirmed-when |
|---|---|---|
| Default/root CAs | `openssl verify -CAfile` chain trace (own infra) | private CA in device trust store |
| Key reuse | `rsactftool` / `openssl` modulus gcd across own keys | shared modulus / reused p,q |
| Weak exponents | `openssl rsa -text` on own key | e=3 / small d |
| Cert pasting | `certigo` own-host chain dump | mismatched SAN/CN for the name |

## TLS protocol-layer classes

| Probe | Test | Confirmed-when |
|---|---|---|
| Version floor | `testssl -p` (own host) | TLS≤1.1 accepted |
| Padding oracle | `sslyze --padding-oracle` own TLS endpoint | BO-like oracle (never active attack) |
| Heartbleed check | `ssl-heartbleed` NSE on own endpoint | critical exposure marker |
| CCS injection | `ssl-ccs-injection` NSE (own endpoint) | ambiguous response |
| SWEET32 | `ssl-enum-ciphers` 64-bit suites (own) | 3DES negotiated |
| POODLE | `ssl-poodle` NSE (own SSLv3 endpoint) | CBC+SSLv3 accepted |
| DROWN | `sslv2-drown` NSE (own host) | SSLv2 + shared key |
| ALPN/SNI | `tlsx -alpn -sni` (own) | protocol confusion surface |

## JWT & session-token crypto

| Probe | Test | Confirmed-when |
|---|---|---|
| alg=none | `jwt_tool -M none` on OWN issued token | none accepted |
| HS/RS confusion | `jwt_tool -X k` (own public key as HMAC) | signature verified with pubkey bytes |
| Weak HMAC | `hashcat -m 16500` on own token | secret cracked |
| kid/path trick | `jwt_tool` kid traversal (own token) | file-read marker |
| jku/x5u open | `jwt_tool -M pb` (own token) | attacker-supplied JWKS accepted (lab) |

## Hashing & password storage

| Probe | Test | Confirmed-when |
|---|---|---|
| Hash identification | `name-that-hash` on OWN dump | plaintext-friendly scheme (md5, lm) |
| Salt presence | `hashid -m` + `john --show` on own dump | unsalted scheme |
| Fast-hash brute | `hashcat` benchmark on own dump (mode table) | runtime < policy floor |
| Length-extension | `hashpump`-class tool on own MAC | length-extendable construction (lab) |

## Cipher-mode & padding classes

| Probe | Test | Confirmed-when |
|---|---|---|
| ECB detect | duplicate ciphertext blocks on own oracle | ECB (blocks repeat) |
| CBC bitflip | flip own token byte, observe oracle | predictable plaintext change |
| IV reuse | capture two own sessions | identical IV across messages |
| Padding oracle (app) | `padbuster` on OWN app endpoint (lab) | oracle distinguishes padding |
| Nonce reuse | two own encryptions same nonce | keystream collision |

## RNG & entropy

| Probe | Test | Confirmed-when |
|---|---|---|
| Predictable tokens | collect own session tokens, `ent` analysis | low entropy / sequential |
| Kernel entropy | `cat /proc/sys/kernel/random/entropy_avail` (own host) | critically low |
| rand() seeds | `crackle`-class on own BLE pairing frames (own device) | predictable MIC |

Walls: hash/token/key material is the OPERATOR'S OWN (dumps from own estate,
tokens issued to the operator, keys the operator holds). Cracking runs only
against own material. No ciphertext the operator does not legitimately hold.