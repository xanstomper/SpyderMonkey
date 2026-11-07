# TLS protocol-layer classes — worker / expired

- source canon: `spydermonkey/crypto-canon.md`
- base technique: `spydermonkey-crypto-canon-tls-protocol-layer-classes.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **worker** · auth **expired** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

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

## Probe adjustment (worker × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
