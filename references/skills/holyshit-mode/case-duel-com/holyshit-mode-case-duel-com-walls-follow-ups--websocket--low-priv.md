# Walls + follow-ups — websocket / low-priv

- source canon: `holyshit-mode/case-duel-com.md`
- base technique: `holyshit-mode-case-duel-com-walls-follow-ups.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **low-priv** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- **Register = GEO-blocked for US IPs** (CF "IP or Country blocked" on all register paths) — note the irony: `friendly_captcha` was DISABLED and `skip_email_verification_requirement` ENABLED (both from the public metadata), so the auth gates were open but geography closed the probe-account door. Do not VPN around geo-controls.
- Two operator-gated follow-ups: (1) a test session → authed chain (chat identify, tips, KYC, PvP arena); (2) `VITE_PAYMENTIQ_TEST:"1`" impact review by their payment team — the single highest-impact config item on the ledger.

## Probe adjustment (websocket × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
