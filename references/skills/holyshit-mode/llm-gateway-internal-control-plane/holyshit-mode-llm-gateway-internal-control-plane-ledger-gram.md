# Ledger grammar (from this run)

- source canon: `holyshit-mode/llm-gateway-internal-control-plane.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `holyleadger chain` splits steps on the **unicode `→`**; keep the impact text free of arrows or
  you get 1 empty step. (Duplicated-chain files surfaced this run.)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
