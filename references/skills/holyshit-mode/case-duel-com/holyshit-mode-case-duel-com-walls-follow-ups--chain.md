# Walls + follow-ups — chain composition

- source canon: `holyshit-mode/case-duel-com.md`
- base technique: `holyshit-mode-case-duel-com-walls-follow-ups.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **Register = GEO-blocked for US IPs** (CF "IP or Country blocked" on all register paths) — note the irony: `friendly_captcha` was DISABLED and `skip_email_verification_requirement` ENABLED (both from the public metadata), so the auth gates were open but geography closed the probe-account door. Do not VPN around geo-controls.
- Two operator-gated follow-ups: (1) a test session → authed chain (chat identify, tips, KYC, PvP arena); (2) `VITE_PAYMENTIQ_TEST:"1`" impact review by their payment team — the single highest-impact config item on the ledger.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
