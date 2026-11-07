# DNS rebinding shape

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

TOCTOU between resolve and fetch — characterized in the lab replica (rebinding needs your own authoritative DNS). The live test registers the TOCTOU hypothesis with the fetch-time evidence you can observe.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
