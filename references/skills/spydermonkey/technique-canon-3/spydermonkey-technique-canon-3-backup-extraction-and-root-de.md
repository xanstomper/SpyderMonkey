# Backup extraction and root-detection gaps

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

allowBackup=true and client-only root/jail checks. Decisive test: adb backup pull of your build; the bypass shim on your device — the class is the check's client-side placement.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
