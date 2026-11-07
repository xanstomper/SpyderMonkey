# 5. Register + report

- source canon: `spydermonkey/tls-auth-audit.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Ledger rows: flat v2 schema (see SKILL.md State & Egress), proof carrying
  literal `baseline: … attack: … diff: …` sections.
- Report shape: TLS table (host × protocol × cert × headers) + auth-architecture
  summary (bearer type, storage, rotation, WS auth material) + hypothesis
  section clearly separated from confirmed findings.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
