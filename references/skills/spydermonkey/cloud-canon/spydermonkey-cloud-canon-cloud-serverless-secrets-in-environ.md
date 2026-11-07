# Cloud Serverless Secrets in Environment (CLOUD-LAMBDA-02)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-07

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: plaintext secrets in function config
- probe: read-only config inventory of the declared functions
- wall: secrets are redacted in the ledger

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
