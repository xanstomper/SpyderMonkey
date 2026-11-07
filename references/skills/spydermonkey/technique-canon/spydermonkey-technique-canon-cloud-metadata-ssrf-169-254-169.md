# Cloud metadata SSRF (169.254.169.254)

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

SSRF reaching instance metadata = the class. Decisive test: SSRF response carrying instance-id/ami-id (hypothesis-grade until a 3-gate diff) — IMDSv2 token-required = the mitigated negative, bank it.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
