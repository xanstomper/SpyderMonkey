# Redirect-based SSRF

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-INPV-10** · **CWE-918** · **ATT&CK T1190**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

An open redirect chains an SSRF-protected fetch past the allowlist. Decisive test: SSRF-prone param → in-scope redirector → internal marker URL — the fetch following the redirect IS the proof (one hop, read-only).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
