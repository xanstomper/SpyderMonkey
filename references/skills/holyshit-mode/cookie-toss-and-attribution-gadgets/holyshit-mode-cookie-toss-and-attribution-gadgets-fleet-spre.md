# Fleet spread

- source canon: `holyshit-mode/cookie-toss-and-attribution-gadgets.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Inventory EVERY mirror/sibling domain's tracker hosts — the gadget is copy-pasted per brand.
One confirmed gadget on the primary + one on any mirror = fleet-wide claim.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
