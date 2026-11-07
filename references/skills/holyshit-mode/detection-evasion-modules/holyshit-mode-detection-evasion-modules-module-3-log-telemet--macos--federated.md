# MODULE 3 — LOG & TELEMETRY EVASION — macos / federated

- source canon: `holyshit-mode/detection-evasion-modules.md`
- base technique: `holyshit-mode-detection-evasion-modules-module-3-log-telemet.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **macos** · auth **federated** · chain role **pivot**

## Route

- probes: `smbclient`, `rpcclient`, `ldapsearch`, `netexec`, `enum4linux`, `kerbrute`, `smbmap`, `nmap-smb-security`
- chains: `win`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: darwin surface — read-only inventory first; the documented class applies to the same daemon/services layer
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

**Objective**: validate SIEM/UEBA detection of anti-forensic techniques.

**Techniques**:
- **Log tampering**: clear Windows event log (wevtutil), truncate Linux auth.log, delete
  SIEM forwarder logs. Validate: does the SIEM alert on log-source silence or only on
  event content?
- **Timestomping**: modify MAC times on payload files to blend with system files.
  Validate: does file-integrity monitoring flag timestamp changes or only content?
- **Artifact wiping**: secure-delete tools, USN journal deletion, prefetch wiping.
  Validate: does the EDR/SIEM correlate deletion events with prior process telemetry?
- **Parent-PID spoofing**: spawn payload under a trusted parent (explorer.exe, svchost).
  Validate: does the EDR validate PPID chains or only the executable hash?

**Detection surface to report**: SIEM log-source heartbeat, file-integrity monitoring,
USN journal analysis, process-tree analytics, UEBA anomaly baselines.

---

## Probe adjustment (macos × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
