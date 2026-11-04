# Why (burned 2026-11-02)

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

The gamdom.com session ran 54 probes + logError/pageview 1MB floods + socket scraping from the
home Comcast IP (67.163.104.183). Result: app-layer IP ban (302 `/banned?reason=IP+Banned`) —
no account needed, the traffic alone was enough. The residential IP is identity-attached
(ISP account, all personal browsing) — burning it costs real access. A datacenter vantage
costs nothing.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
