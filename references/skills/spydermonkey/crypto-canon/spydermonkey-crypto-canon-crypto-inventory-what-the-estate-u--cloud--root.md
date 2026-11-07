# Crypto inventory — what the estate uses — cloud / root

- source canon: `spydermonkey/crypto-canon.md`
- base technique: `spydermonkey-crypto-canon-crypto-inventory-what-the-estate-u.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **cloud** · auth **root** · chain role **pivot**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Cert inventory | `sslscan`/`testssl` + `openssl x509` on owned hosts | key size < 2048 / sha1 / expiring soon |
| Cipher survey | `testssl --cipher-per-proto` on own targets | RC4/3DES/null/anon suites present |
| Curve check | `openssl s_client -groups` on own host | secp256r1-only or weak curves |
| HSTS/forward secrecy | `tlsx -hsts` + key-exchange list | no PFS, no HSTS |
| Session resumption | `sslyze --resum` | ticket/no-resumption anomalies |

## Probe adjustment (cloud × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
