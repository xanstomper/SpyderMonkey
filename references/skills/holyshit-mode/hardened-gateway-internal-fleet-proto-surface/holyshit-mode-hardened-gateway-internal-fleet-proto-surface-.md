# Contrast vs the vulnerable GoTrue variant (example-target/example-target)

- source canon: `holyshit-mode/hardened-gateway-internal-fleet-proto-surface.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

The earlier findings (redirect_uri forwarded verbatim, anon key client-exposed, unthrottled code
exchange) come from an **un-hardened GoTrue deployment**. Always fingerprint BEFORE assuming: server-side
PKCE + no client anon key + hardcoded redirect_to ⇒ the example-target chain does not apply; pivot.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
