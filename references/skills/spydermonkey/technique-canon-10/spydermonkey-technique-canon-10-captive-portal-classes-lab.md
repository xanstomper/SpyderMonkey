# Captive-portal classes (lab)

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **WSTG-INPV-06** · **CWE-601** · **ATT&CK T1190**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Lab captive-portal redirect behavior characterization only. Decisive test: your lab portal's redirect path = the class row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
