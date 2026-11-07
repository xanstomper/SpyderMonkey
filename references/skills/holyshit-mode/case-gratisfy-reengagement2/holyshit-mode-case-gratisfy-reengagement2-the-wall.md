# The wall

- source canon: `holyshit-mode/case-gratisfy-reengagement2.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Every remaining path needs either (a) an app endpoint that trusts `user_metadata.role`, or (b) OTP TTL >> brute time (needs ~10× throughput). GoTrue redirect_uri override remains confirmed-but-blocked at Discord (strict URI registration; live listener test = Discord "Invalid OAuth" rejection).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
