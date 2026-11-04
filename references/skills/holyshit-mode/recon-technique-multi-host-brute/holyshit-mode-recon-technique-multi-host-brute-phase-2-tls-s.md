# Phase 2: TLS + SAN Extraction

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## The technique

- OpenSSL `s_client -connect` cert SAN revealed: `openinfra.f***REDACTED***.org`, `*.opendata.f***REDACTED***.org`
- These internal infra hosts are not linked from the public site — SAN extraction is the only discovery vector
- Technique: `openssl s_client -connect f***REDACTED***.org:443 -servername f***REDACTED***.org`

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
