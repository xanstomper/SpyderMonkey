# MFA grace-window and trusted-device abuse

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-ATHN-09** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

"Remember this device" tied to a long-lived cookie outlives the OTP it certified. Decisive test: complete MFA once, capture the device cookie, and read its expiry + behavior after password change — MFA bypassed by a stolen cookie is the finding (characterize on your own principal).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
