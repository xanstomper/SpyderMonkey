# WAF vantage burn and recovery (the reusable recipe) — container / high-priv

- source canon: `holyshit-mode/case-duelbits-com.md`
- base technique: `holyshit-mode-case-duelbits-com-waf-vantage-burn-and-recover.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **high-priv** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Aggressive CF configs flag a scripted vantage MID-ROUND: the same path alternates 200/403,
  then every path turnstile-challenges — including hosts that were open an hour earlier and
  even a real-browser harness (managed challenge, not auto-passing). Budget for it; the burn
  is not a wall on the TARGET, it is a wall on YOUR VANTAGE.
- **The burn persists across days and spreads across the brand family.** Host differentials
  recorded pre-burn DECAY: before trusting any "this sibling was unchallenged" note, spend ONE
  navigation re-verifying it — do not re-probe per host. A challenged nav (title "Just a
  moment…") also poisons every in-page fetch: XHR fails with a NetworkError that masquerades
  as a different bug. Check the page title before running in-page probes, and never use the
  CDP browser as burn recovery — on a burned IP the managed challenge does not auto-pass for
  it either; the only clean vantage left is the operator's own logged-in console.
- Recovery pivots that worked, in order:
  1. **Find one unchallenged path** — SPA fallbacks often exempt utility paths
     (`/.well-known/openid-configuration` served the full 78KB SPA shell unchallenged). The
     shell carries the complete asset list: 200+ chunk names incl. the config chunks.
  2. **Wayback CDX index** (`web.archive.org/cdx/search/cdx?url=<domain>/*&output=json&collapse=urlkey`)
     = the captured-URL inventory without touching the live WAF. Reveals endpoint names the
     live site hides (the OIDC path) and the asset history. The availability API and direct
     page fetches rate-limit (429) fast — the CDX query is the one that pays.
  3. **crt.sh for the subdomain fleet** (64 hosts here) when the live surface is walled —
     CT logs never trip the WAF.
  4. web_extract as a different egress for archive pages.
- Dev-tier subdomains (admin-dev, admin-staging, chadmin-*, chad-api-*, auth/wallet/pay/gs/ws
  dev+staging) were CT-visible but challenge/Access-walled — log the fleet map as coverage
  and say what a clean vantage or session unlocks.

## Probe adjustment (container × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
