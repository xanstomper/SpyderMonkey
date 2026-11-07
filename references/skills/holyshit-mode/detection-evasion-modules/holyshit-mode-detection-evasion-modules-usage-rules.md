# USAGE RULES

- source canon: `holyshit-mode/detection-evasion-modules.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Every module requires explicit stealth-validation scope in the authorization document.
- Each technique is run once, logged with timestamp, and reverted immediately after
  validation.
- The output is a detection-gap report: technique → expected detection → observed
  detection → proposed analytic (Sigma/KNQL/CloudWatch rule).
- No module is used against production users or data — lab tenants, test accounts, and
  scoped resources only.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
