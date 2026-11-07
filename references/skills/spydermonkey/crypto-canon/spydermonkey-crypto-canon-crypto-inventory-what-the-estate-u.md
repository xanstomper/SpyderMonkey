# Crypto inventory — what the estate uses

- source canon: `spydermonkey/crypto-canon.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Cert inventory | `sslscan`/`testssl` + `openssl x509` on owned hosts | key size < 2048 / sha1 / expiring soon |
| Cipher survey | `testssl --cipher-per-proto` on own targets | RC4/3DES/null/anon suites present |
| Curve check | `openssl s_client -groups` on own host | secp256r1-only or weak curves |
| HSTS/forward secrecy | `tlsx -hsts` + key-exchange list | no PFS, no HSTS |
| Session resumption | `sslyze --resum` | ticket/no-resumption anomalies |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
