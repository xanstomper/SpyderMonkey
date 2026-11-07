# Citations rot: check the current manifest before testing a claimed artifact

- source canon: `spydermonkey/engagement-ops.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Public claims name files by build hash (`Crash.route.BBLHNSNC.js`). Builds rotate weekly;
resolve CURRENT chunk names from the live index/route manifest (`grep -oE
"[A-Za-z]+\.route\.[A-Za-z0-9_-]{8}\.js" client.<hash>.js`) before declaring a file
missing or testing its contents. A cited artifact's absence after rotation is a finding
(evidence rotated post-exposure); scanning ~800KB of current chunks for the claimed math
(sha256/2**52/slice(0,13)/hardcoded 64-hex) and finding none is the testable half.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
