# Hardcoded key inventory

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

API keys/signing secrets embedded in binary or resources. Decisive test: string scan pairing the key with its live use-site = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
