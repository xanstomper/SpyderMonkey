# MODULE 5 — CLOUD & CONTAINER TRADECRAFT

- source canon: `holyshit-mode/detection-evasion-modules.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-07

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

**Objective**: validate cloud-native detection of lateral movement and privilege escalation.

**Techniques**:
- **Instance-metadata credential theft**: query IMDSv1 on a lab instance, use creds from
  external IP. Validate: does CloudTrail flag credential-use from external IPs or only
  internal API calls?
- **Container escape**: privileged container → host mount → root. Validate: does the
  container runtime flag mount escapes or only process anomalies?
- **Serverless persistence**: modify Lambda env vars, insert CloudWatch event rules.
  Validate: does CloudTrail flag config changes or only API calls?
- **Cross-account role assumption**: assume role in lab account B from account A without
  external ID. Validate: does CloudTrail flag cross-account assumptions or only same-account?
- **Kubernetes lateral movement**: exploit over-permissive RBAC to list secrets in all
  namespaces. Validate: does the K8s audit log flag bulk secret access or only pod exec?

**Detection surface to report**: CloudTrail event selectors, GuardDuty/Security Hub
findings, K8s audit-log analysis, container runtime security, IAM anomaly detection.

---

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
