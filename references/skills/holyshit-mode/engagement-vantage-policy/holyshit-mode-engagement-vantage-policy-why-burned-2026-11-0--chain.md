# Why (burned 2026-11-02) — chain composition

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- base technique: `holyshit-mode-engagement-vantage-policy-why-burned-2026-11-0.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The g***REDACTED***.com session ran 54 probes + logError/pageview 1MB floods + socket scraping from the
home Comcast IP (67.163.104.183). Result: app-layer IP ban (302 `/banned?reason=IP+Banned`) —
no account needed, the traffic alone was enough. The residential IP is identity-attached
(ISP account, all personal browsing) — burning it costs real access. A datacenter vantage
costs nothing.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
