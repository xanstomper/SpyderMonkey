# Ceiling verdict (2026-11-03 closeout of the autonomous phase) — chain composition

- source canon: `holyshit-mode/case-rainbet-com.md`
- base technique: `holyshit-mode-case-rainbet-com-ceiling-verdict-2026-11-03-cl.md`
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

- **Region block = absolute for the DE vantage.** 8 runner cycles: the wallet-verify returns
  `451 er_sign_up_region_block` for plain AND restricted variants; the `ssr-client-ip` /
  `country` / `region` SSR headers are IGNORED (region = CF-IPCountry-derived). Email signup =
  Turnstile + edge challenge. No session without a non-blocked egress or an operator session.
- **Socket auth = server-bound.** `/player-bets` connects with a client-asserted
  `x-public-id` (a victim's real 32-char id) are silently dropped from guest connections —
  the claim is derived from the session server-side. Opt-out (stats:0) is respected on both
  the profile and the history endpoints — the financial-dump finding was re-rated 70→55.
- Demo mode = preview-only for guests; no unauth game flow.
- DMARC `p=quarantine`, SPF `~all`, 25/50 historical subdomains clean-NXDOMAIN (no dangling
  CNAMEs, no takeovers); rbtmq droplets mid-decommission (DNS deleted, droplet alive by IP);
  `staging-mono` ELB orphaned.

**The "they'd feel it" finding = the toss+fingerprint combo**: FingerprintJS Pro (a paid
service) is defeated by a 40-byte URL param on their own media host — device-ban evasion +
attribution/affiliate hijack via any link. That is the headline of the disclosure package.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
