# Final state

- source canon: `holyshit-mode/case-obsidian-y-api-reengage5-provider-wiring.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `http://localhost:8620` playground; `http://10.0.0.142:8620/v1` LAN API; any key works.
- Hermes provider `obsidian-free` + 2-entry fallback chain. 30 live models, 27 tool-capable.
- holyleadger next-actions for this target: treat pg_shared_context/poisoning as decayed —
  re-verify with fresh PTOK drift before re-asserting.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
