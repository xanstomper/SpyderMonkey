# Dangling CNAME / subdomain takeover

- source canon: `spydermonkey/technique-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

CNAME to NXDOMAIN + claimable service = takeover prep. Decisive test: cname → resolution failure + the target service's fingerprint (e.g. "There isn't a GitHub Pages site here") = the class. Register the claimability, never claim a third-party domain you lack rights to.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
