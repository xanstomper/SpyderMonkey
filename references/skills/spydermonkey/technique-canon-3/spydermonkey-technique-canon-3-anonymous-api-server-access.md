# Anonymous API server access

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`/api/v1/...` unauthenticated or system:anonymous-bound. Decisive test: GET /api/v1/namespaces anonymous — a 200 listing = the finding (read-only inventory only).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
