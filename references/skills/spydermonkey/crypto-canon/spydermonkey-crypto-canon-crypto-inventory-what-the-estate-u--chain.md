# Crypto inventory — what the estate uses — chain composition

- source canon: `spydermonkey/crypto-canon.md`
- base technique: `spydermonkey-crypto-canon-crypto-inventory-what-the-estate-u.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Probe | Test | Confirmed-when |
|---|---|---|
| Cert inventory | `sslscan`/`testssl` + `openssl x509` on owned hosts | key size < 2048 / sha1 / expiring soon |
| Cipher survey | `testssl --cipher-per-proto` on own targets | RC4/3DES/null/anon suites present |
| Curve check | `openssl s_client -groups` on own host | secp256r1-only or weak curves |
| HSTS/forward secrecy | `tlsx -hsts` + key-exchange list | no PFS, no HSTS |
| Session resumption | `sslyze --resum` | ticket/no-resumption anomalies |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
