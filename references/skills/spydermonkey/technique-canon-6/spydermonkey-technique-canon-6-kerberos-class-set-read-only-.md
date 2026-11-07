# Kerberos class set (read-only enum)

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

AS-REP-roastable accounts, kerberoastable SPNs, unconstrained-delegation CONFIG exposure — all ENUMERABLE read-only (canon-III); the crack/capture stays the no-gain wall. Decisive test: enum output naming the accounts — the list is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
