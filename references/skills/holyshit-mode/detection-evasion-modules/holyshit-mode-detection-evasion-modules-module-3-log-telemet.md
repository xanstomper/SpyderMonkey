# MODULE 3 — LOG & TELEMETRY EVASION

- source canon: `holyshit-mode/detection-evasion-modules.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `smbclient`, `rpcclient`, `ldapsearch`, `netexec`, `enum4linux`, `kerbrute`, `smbmap`, `nmap-smb-security`
- chains: `win`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
