# Hardened-LLM-gateway fast re-engagement ladder (all fresh, live, ~40 requests)

- source canon: `holyshit-mode/compromise-vs-observation-and-hardened-gateway-reengagement.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

When re-engaging a gateway whose proxy-layer surface was previously "confirmed" but which
you suspect is actually hardened, run THIS set — it decisively closes the compromise classes:

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
