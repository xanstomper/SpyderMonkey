# D5 — CRAFTED-PoC (the forge)

- source canon: `undercroft/undercroft-playbook.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Every finding ships as: `class · request (one line) · proof (one line) · Δ · impact`.
Register in `undercroft state` (craft) and hand to 3AM: `learn` the vector, `promote`
into the living matrix when verified. The family only gets faster campaign-over-
campaign; UNDERCROFT is the vector forge that feeds it.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
