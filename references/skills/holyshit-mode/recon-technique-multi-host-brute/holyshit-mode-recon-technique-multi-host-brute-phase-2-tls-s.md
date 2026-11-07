# Phase 2: TLS + SAN Extraction

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- OpenSSL `s_client -connect` cert SAN revealed: `openinfra.f***REDACTED***.org`, `*.opendata.f***REDACTED***.org`
- These internal infra hosts are not linked from the public site — SAN extraction is the only discovery vector
- Technique: `openssl s_client -connect f***REDACTED***.org:443 -servername f***REDACTED***.org`

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
