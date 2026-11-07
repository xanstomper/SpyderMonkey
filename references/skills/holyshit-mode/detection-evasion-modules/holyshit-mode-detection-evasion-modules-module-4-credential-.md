# MODULE 4 — CREDENTIAL & IDENTITY TRADECRAFT

- source canon: `holyshit-mode/detection-evasion-modules.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

**Objective**: validate identity-threat detection of credential attacks.

**Techniques**:
- **Password spraying**: 1 password × N users (not 1 user × N passwords) from a single
  source IP, low-and-slow (1 attempt/min). Validate: does the IdP flag spray patterns or
  only per-user lockouts?
- **Token impersonation**: steal a session token from a lab browser profile, replay from
  different IP/UA. Validate: does the IdP flag token reuse or only credential mismatches?
- **Kerberoasting**: request RC4-encrypted service tickets for SPN accounts, crack offline.
  Validate: does the DC flag encryption-downgrade or only abnormal TGS volume?
- **Pass-the-hash/ticket**: reuse NTLM hash or Kerberos ticket on lab hosts. Validate:
  does the EDR flag hash-reuse patterns or only logon type anomalies?

**Detection surface to report**: IdP risk analytics, DC anomaly detection, Kerberos
encryption policy, token-binding enforcement, UEBA credential-behavior baselines.

---

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
