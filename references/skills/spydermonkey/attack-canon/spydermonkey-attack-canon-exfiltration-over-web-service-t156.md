# Exfiltration Over Web Service (T1567)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-BUSL-02** · **CWE-840** · **ATT&CK T1565**
- generated: 2026-11-04

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: data out through trusted clouds
- probe: never exercised; the IMPACT LEG is priced by shukaku instead
- wall: NO-GAIN — exfiltration is priced hypothetically, never performed

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
