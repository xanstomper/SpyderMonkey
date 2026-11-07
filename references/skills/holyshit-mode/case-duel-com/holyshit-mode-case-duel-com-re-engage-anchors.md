# Re-engage anchors

- source canon: `holyshit-mode/case-duel-com.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `VITE_BUILD_COMMIT` in the env object (this session: `22aa5245`) = the bundle-hash diff oracle.
- Re-verify first: profile financial fields, socket anon streaming, PaymentIQ test flag. `next --target duel.com` surfaces them.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
