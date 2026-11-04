# Walls + follow-ups

- source canon: `holyshit-mode/case-duel-com.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- **Register = GEO-blocked for US IPs** (CF "IP or Country blocked" on all register paths) — note the irony: `friendly_captcha` was DISABLED and `skip_email_verification_requirement` ENABLED (both from the public metadata), so the auth gates were open but geography closed the probe-account door. Do not VPN around geo-controls.
- Two operator-gated follow-ups: (1) a test session → authed chain (chat identify, tips, KYC, PvP arena); (2) `VITE_PAYMENTIQ_TEST:"1`" impact review by their payment team — the single highest-impact config item on the ledger.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
