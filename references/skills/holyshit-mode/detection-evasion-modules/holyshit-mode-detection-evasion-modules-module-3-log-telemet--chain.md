# MODULE 3 — LOG & TELEMETRY EVASION — chain composition

- source canon: `holyshit-mode/detection-evasion-modules.md`
- base technique: `holyshit-mode-detection-evasion-modules-module-3-log-telemet.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
