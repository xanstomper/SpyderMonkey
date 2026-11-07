# Fixes to recommend

- source canon: `holyshit-mode/cookie-toss-and-attribution-gadgets.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Allowlist (not blocklist) writable params; refuse writes matching session-family prefixes;
signed/short-lived attribution tokens validated server-side at signup; treat identity cookies
as untrusted client input and re-verify server-side before risk decisions.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
