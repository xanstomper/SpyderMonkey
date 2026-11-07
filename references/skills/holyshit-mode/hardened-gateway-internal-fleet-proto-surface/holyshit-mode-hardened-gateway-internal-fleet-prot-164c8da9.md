# Honest ceiling

- source canon: `holyshit-mode/hardened-gateway-internal-fleet-proto-surface.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

The worker pods are self-contained: no SSRF (`url`/`base_url`/`endpoint` params ignored or time out),
no IMDS/cloud-metadata reach, no `/v1/keys` mint, no RCE. Escalation to key-mint / org-admin / BYOK-secret
drain requires passing the auth wall (authenticated context). When the operator insists "there's
definitely a way past", re-probe the auth surface fresh; if genuinely hardened, record a **negative**
(`auth_wall_hardened_no_bypass`) and state the ceiling — never fabricate a forge or escalation.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
