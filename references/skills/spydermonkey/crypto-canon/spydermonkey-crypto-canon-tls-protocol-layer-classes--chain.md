# TLS protocol-layer classes — chain composition

- source canon: `spydermonkey/crypto-canon.md`
- base technique: `spydermonkey-crypto-canon-tls-protocol-layer-classes.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
