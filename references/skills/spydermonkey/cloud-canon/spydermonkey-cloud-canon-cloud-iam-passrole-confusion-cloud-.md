# Cloud IAM PassRole Confusion (CLOUD-IAM-02)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **WSTG-BUSL-02** · **CWE-840** · **ATT&CK T1565**
- generated: 2026-11-07

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: a principal that can pass a role to a service it controls
- probe: read-only path analysis of role trust + pass grants — the CHAIN is priced, never walked
- wall: NO-GAIN — the escalation path is a ledger row, not an action

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
