# 6. Post-breach user-protection checks (do these even when the core is clean) — chain composition

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- base technique: `holyshit-mode-case-gamdom-adjacent-infra-6-post-breach-user-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `dig TXT _dmarc.<domain>` — `p=reject; pct=100` = spoofing dead. `p=none` or missing =
  post-breach phishing is trivially easy and becomes a critical finding.
- Full SPF (`-all` vs `~all`) + DKIM selector sweep (`default|google|s1|s2|selector1...`).
- The breach data itself drives phishing lures; the email-auth posture decides whether
  attackers can send AS the domain. This is the live risk while the extortion clock runs.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
