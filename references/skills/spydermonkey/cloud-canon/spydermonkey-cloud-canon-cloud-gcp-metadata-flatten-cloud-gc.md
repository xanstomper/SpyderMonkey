# Cloud GCP Metadata Flatten (CLOUD-GCP-02)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **WSTG-INPV-10** · **CWE-918** · **ATT&CK T1190**
- generated: 2026-11-04

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: metadata endpoint reach via SSRF
- probe: SSRF battery metadata targets
- wall: proof-of-reach only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
