# TECHNIQUE CANON XIII — ASVS verification canon (controls as offensive checks)

_Every block maps an ASVS control family to its VERIFICATION probe: how an authorized tester proves the control's absence. Validation-only, NO-GAIN. Feeds skilltree.py._

## Authentication verification

### Password-security verification
Server-enforced length/complexity/newness tested by one policy-violating change. Decisive test: acceptance on your account = control absent.

### Brute-force-resistance verification
Lockout/rate geometry measured (the canon-I discipline). Decisive test: the counter/lock TTL map = the control's presence/absence.

### Recovery-flow verification
Reset/change flows single-use, entropy-checked, host-safe (canon-I depth). Decisive test: replay + poisoning on your own inbox = the absence.

### Session-termination verification
Logout/password-change kills server state. Decisive test: post-logout replay on your session = the absence.

## Session verification

### Token-generation verification
Entropy/structure math on your own tokens (canon-VI). Decisive test: sub-threshold entropy = the control absent.

### Token-validation verification
Server-side validation of signature/expiry/audience. Decisive test: forged-but-benign acceptance = the absence.

### Renewal/invalidation verification
Rotation on privilege change; old tokens dead. Decisive test: pre-privilege token alive after = the absence.

## Authorization verification

### Object-level verification
The BOLA differential per object type (canon-VIII). Decisive test: cross-id content echo = the absence.

### Function-level verification
Admin actions via direct API with low-priv token. Decisive test: acceptance = the absence.

### Data-field-level verification
Write-path field filtering (the mass-assign twin). Decisive test: hidden sensitive field accepted on your record = the absence.

## Data-protection verification

### Transport-protection verification
Cleartext-sensitive and weak-TLS lanes (canon-I/XI). Decisive test: the captured cleartext / cipher row = the absence.

### Data-at-rest verification
Sensitive material unencrypted in backend stores — provable only from confirmed footholds (kaisha-priced) or client mirrors. Decisive test: the mirrored artifact's plaintext = the absence.

### PII-minimization verification
Responses returning more PII than the UI uses. Decisive test: the response-field diff vs the rendered need = the absence.

## Communications verification

### TLS-only enforcement
http→https redirect + HSTS on every tier. Decisive test: the http variant serving content = the absence.

### Header-policy verification
CSP/HSTS/X-Frame/X-Content-Type/Referrer-Policy matrix (the header-posture canon). Decisive test: the posture matrix = the rows.

### Certificate-pinning verification (mobile tier)
Pinning presence/placement (canon-XII). Decisive test: local-CA acceptance on your build = the absence.

## Malicious-input verification

### Injection-verification set
SQLi/NoSQL/LDAP/cmd/SSTI/XXE decisive oracles (canon-II full depth). Decisive test: the oracle delta per class = the absence.

### Upload-verification set
Type/content/path validation (canon-XI). Decisive test: benign-marker acceptance = the absence.

### Deserialization-verification set
OOB-DNS gadget proofs (canon-II discipline). Decisive test: the lookup arrival = the absence.

## Error & logging verification

### Error-disclosure verification
Stack traces/config in errors (canon-IX). Decisive test: forced-error content = the absence.

### Audit-log verification (external signal)
Missing log coverage inferred from unlogged test actions visible server-side — provable only from the operator's own visibility; characterize as hypothesis-grade from client-visible traces. Decisive test: none without operator logs — the honest ceiling row.

## Business-logic verification

### Flow-integrity verification
Multi-step flows skippable/reorderable (the flow gate's canon). Decisive test: the skip/reorder completing on your test flow = the absence.

### Limit-integrity verification
Rate/budget/entitlement caps enforced server-side (canon-III abuse depth). Decisive test: the cap-dodge arithmetic = the absence.

### Anti-automation verification
Anti-bot/captcha posture mapping (canon-VI anatomy). Decisive test: the treatment matrix = the row.
