# MODULE 5 — CLOUD & CONTAINER TRADECRAFT — browser / machine

- source canon: `holyshit-mode/detection-evasion-modules.md`
- base technique: `holyshit-mode-detection-evasion-modules-module-5-cloud-conta.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **browser** · auth **machine** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (browser × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
