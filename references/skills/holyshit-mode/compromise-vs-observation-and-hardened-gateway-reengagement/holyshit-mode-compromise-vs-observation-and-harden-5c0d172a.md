# Relationship to prior sessions

- source canon: `holyshit-mode/compromise-vs-observation-and-hardened-gateway-reengagement.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

The obsidian ledger's top-scored items (cross-user poisoning 95, shared-buffer disclosure 85)
were genuine compromises on 2026-10-05 but are now PATCHED (PTOK constant). Re-asserting them
as current findings without a fresh PTOK-drift test would be a stale-finding error. The
data-plane session (case-obsidian-y-api-dataplane.md) added observation-class findings; this
is the compromise-scored companion.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
