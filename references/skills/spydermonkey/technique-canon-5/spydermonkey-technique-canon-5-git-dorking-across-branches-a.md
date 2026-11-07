# Git-dorking across branches and dangling objects

- source canon: `spydermonkey/technique-canon-5.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`git log --all --diff-filter=D`, dangling blobs via rev-list --objects, deleted verify pages recoverable. Decisive test: the recovered object content — provenance-stamped.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
