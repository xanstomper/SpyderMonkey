# IIS short-name (8.3) enumeration

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`~1` short-name requests enumerate files/dirs despite listing denial. Decisive test: /~s/~1 style probes yielding distinct 404-vs-200 classes for the control vs candidate — the oracle is the finding (read-only inventory).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
