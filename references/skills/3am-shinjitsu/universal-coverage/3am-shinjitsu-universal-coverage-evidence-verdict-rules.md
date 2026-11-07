# Evidence & verdict rules

- source canon: `3am-shinjitsu/universal-coverage.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- **CONFIRMED** requires an authorized, minimal, non-destructive proof and a control check.
- **BLOCKED** means authorization, vantage, or tooling stopped the decisive test; name it.
- **HYPOTHESIS** means reasoned but unproven; include the exact gap and unlock condition.
- **N/A** requires a concrete reason (e.g. "no AI components deployed; inventory export
  dated 2026-11-03 confirms zero inference endpoints").
- Secrets are redacted in reports. Read-only access is used only to prove impact.
- Findings decay; record deployed version/build and re-verify before reuse.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
