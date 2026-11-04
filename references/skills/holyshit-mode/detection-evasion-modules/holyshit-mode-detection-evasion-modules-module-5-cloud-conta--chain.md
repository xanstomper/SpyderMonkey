# MODULE 5 — CLOUD & CONTAINER TRADECRAFT — chain composition

- source canon: `holyshit-mode/detection-evasion-modules.md`
- base technique: `holyshit-mode-detection-evasion-modules-module-5-cloud-conta.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
