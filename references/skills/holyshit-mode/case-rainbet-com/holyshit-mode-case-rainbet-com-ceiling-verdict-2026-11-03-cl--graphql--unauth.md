# Ceiling verdict (2026-11-03 closeout of the autonomous phase) — graphql / unauth

- source canon: `holyshit-mode/case-rainbet-com.md`
- base technique: `holyshit-mode-case-rainbet-com-ceiling-verdict-2026-11-03-cl.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **graphql** · auth **unauth** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

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

## Probe adjustment (graphql × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
