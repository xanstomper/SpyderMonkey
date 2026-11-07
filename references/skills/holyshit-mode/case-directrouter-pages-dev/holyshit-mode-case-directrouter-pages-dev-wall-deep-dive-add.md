# Wall — deep dive (added 2026-10-04 evening)

- source canon: `holyshit-mode/case-directrouter-pages-dev.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Discord OAuth session required for `/v1/chat/completions`, `/api/keys`, `/api/redeem`,
`/api/usage/stats`, `/api/auth/me`, `/api/admin/*`. Admin Bearer required for `/api/admin/*`.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
