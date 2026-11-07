# TLS protocol-layer classes

- source canon: `spydermonkey/crypto-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
