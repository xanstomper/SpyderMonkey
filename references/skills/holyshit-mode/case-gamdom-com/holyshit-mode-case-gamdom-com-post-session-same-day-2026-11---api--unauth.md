# Post-session (same day, 2026-11-02): THE BAN — api / unauth

- source canon: `holyshit-mode/case-gamdom-com.md`
- base technique: `holyshit-mode-case-gamdom-com-post-session-same-day-2026-11-.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **api** · auth **unauth** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

The probe traffic got the operator's HOME IP banned at the app layer — `302 /banned?reason=IP+Banned+-+67.163.104.183`, no account involved (pure traffic attribution). Attributed vectors in priority order: (1) logError/pageview 1MB malformed-JSON 20-burst floods (the only abusive-shaped traffic, `x-nginx-limit-req: PASSED` so it's a blocklist entry, not a decay window); (2) 4+ anon EIO=3 socket captures up to 1.4MB + the duplicate-socket sid attach. NOT the cause: perabet/VestaCP port scans (LeaseWeb infra, invisible to gamdom), signup attempts (zero POSTs left the machine), anything published (repo has no gamdom files). Vermes (92.5.99.31) returns clean 200. **All future engagement traffic fires from the VM — `references/engagement-vantage-policy.md`. Never re-probe gamdom from the home IP.**

**2026-11-02 closeout:** disclosure was drafted (home PC `~/gamdom-disclosure-draft.md`: hidden-mode display_username leak + crash hash-chain verification + schema-in-feed, anonymous, via bugs@gamdom.com — gamdom's own FAQ names that intake; no VDP/security.txt exists) but **NOT sent** — operator chose to leave it after the IP ban (engagement intent was goodwill bug-reporting; the ban killed that). The hidden_mode display_username leak therefore remains LIVE/unfixed. If re-engaging ever: test whether the leak still exists first (findings decay), then re-offer the draft — it is send-ready from any anonymous account.

## Probe adjustment (api × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
