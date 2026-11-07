# MODULE 4 — CREDENTIAL & IDENTITY TRADECRAFT — cloud / low-priv

- source canon: `holyshit-mode/detection-evasion-modules.md`
- base technique: `holyshit-mode-detection-evasion-modules-module-4-credential-.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **cloud** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

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

## Probe adjustment (cloud × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
