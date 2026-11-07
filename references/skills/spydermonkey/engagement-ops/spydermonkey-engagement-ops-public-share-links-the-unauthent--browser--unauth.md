# Public share links: the unauthenticated data path AND a retention-expiry oracle — browser / unauth

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-public-share-links-the-unauthent.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **browser** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Players paste hand-share links on public forums (Reddit, 2+2, RUNitOnce) — every pasted link is a working UNAUTH data path and a timestamped probe:

1. **Harvest real share URLs from forums** (`web_search` for the share host + format fragments) to learn the platform's share formats — one estate serves several share TYPES (hand-replay, timeline, embedded image) with DIFFERENT id schemes AND lifetimes.
2. **Load one real link on the VM capturing every XHR** (puppeteer `page.on('response')`, filter `/api/`) — the SPA's own unauthenticated API calls fall out: the share resolver (`/api/share/alias?type=X&alias=Y`) and the data route behind it. The server-RENDERED `<title>` of a share page already leaks hand metadata (game, stakes, tournament id) to anyone — capture it as its own disclosure line.
3. **Decode the alias keyspace OFFLINE before touching the server again**: collect 5+ aliases, decode as base36/base62 big-ints, diff pairwise. Non-sequential magnitudes = random ~114-bit tokens = NOT enumerable — bank the negative row (share keys are strong) and stop mutating aliases; brute-forcing a proven-random keyspace wastes the noise budget.
4. **Re-fetch the OLDEST harvested aliases as the retention test**: a share that outlives the platform's own stated retention (docs claim 90-day downloads; a 4-year-old link still serving full hand data) = a DATA-class finding — permanent public hole-card/nickname exposure keyed by links the players themselves published. Compare share TYPES: some expired, some didn't = inconsistent-expiry discipline, part of the same row.
5. **Evidence even when bodies are encrypted**: (valid alias → 200 + payload size) vs (dead/mutated alias → small error envelope) is the validity oracle — the size delta works without decrypting anything.

## Probe adjustment (browser × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
