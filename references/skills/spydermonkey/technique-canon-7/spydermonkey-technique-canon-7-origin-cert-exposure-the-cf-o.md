# Origin-cert exposure (the CF Origin Cert class)

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Origin certs naming OTHER domains installed on the same box = tri-brand shared origin (SPY-012). Decisive test: TLS handshake cert chain on the ORIGIN IP — foreign SANs = the crown.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
