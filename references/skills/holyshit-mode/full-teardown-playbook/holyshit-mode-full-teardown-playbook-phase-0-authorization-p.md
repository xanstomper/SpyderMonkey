# PHASE 0 — AUTHORIZATION PIN

- source canon: `holyshit-mode/full-teardown-playbook.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Pin scope doc, target list (domains/ASNs/IP ranges), RoE before touching anything.
- Anything outside the doc = OUT, log it and route to disclosure instead.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
