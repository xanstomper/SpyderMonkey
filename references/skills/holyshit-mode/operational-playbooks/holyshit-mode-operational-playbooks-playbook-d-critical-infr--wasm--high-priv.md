# PLAYBOOK D — CRITICAL-INFRASTRUCTURE-ADJACENT (NOT OT/ICS) — wasm / high-priv

- source canon: `holyshit-mode/operational-playbooks.md`
- base technique: `holyshit-mode-operational-playbooks-playbook-d-critical-infr.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **wasm** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

**Scope note**: OT/ICS (SCADA, PLCs, grid systems) are RESTRICTED TARGETS. This playbook
covers adjacent IT: building management systems, logistics platforms, supply-chain portals,
fleet management, smart-city dashboards (non-safety-critical).

**Phase 1 — Recon**
- Separate safety-critical OT networks from business IT via passive DNS + ASN analysis.
- Shodan/Censys for exposed industrial protocols (Modbus, BACnet, DNP3) — flag as
  RESTRICTED, do not touch, report to owner.

**Phase 2 — Access Control**
- Role separation: operator vs supervisor vs auditor — BFLA on privileged actions.
- Shared-account detection: can multiple users share credentials without detection?
- Physical-access integration: badge systems, door controllers — API exposure?

**Phase 3 — Data Integrity**
- Sensor-data validation: can you inject falsified telemetry via API (test with scoped
  simulator, never production sensors)?
- Audit-log integrity: are logs tamper-evident? Can you delete your own entries?
- Time-series manipulation: backdate/forward-date records in historian databases.

**Phase 4 — Supply-Chain Portal**
- Vendor onboarding: document upload → malware scanning → sandbox escape (test with EICAR).
- Purchase-order race conditions: duplicate approvals, split orders to bypass thresholds.
- Invoice tampering: can vendors alter bank details post-approval?

**Deliverable**: IT/OT boundary map, role-authorization findings, data-integrity validation,
supply-chain workflow gaps, exposed-OT report (no touch, disclosure only).

---

## Probe adjustment (wasm × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
