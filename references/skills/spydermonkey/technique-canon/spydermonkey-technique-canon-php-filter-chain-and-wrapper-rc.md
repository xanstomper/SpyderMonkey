# PHP filter chain and wrapper rce-shape

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

php://filter chains (convert.iconv) produce arithmetic-signed output for blind detection. Decisive test: chain produces the expected signature byte pattern — class confirmed read-only.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
