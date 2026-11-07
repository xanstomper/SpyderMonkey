# Phrasing template

- source canon: `holyshit-mode/adhoc-verification-loop.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

> **Ad-hoc verification passed: 7/7, exit 0** (not a suite green — no canonical test/lint config exists here; focused temp script, created/run/cleaned).
> - compile ✓ / synthetic fixture roundtrip ✓ / domain-window sanity ✓ / live end-to-end run ✓
> - First attempt failed on the harness (fixture omitted <field>), not the changed code; fixed and all green.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
