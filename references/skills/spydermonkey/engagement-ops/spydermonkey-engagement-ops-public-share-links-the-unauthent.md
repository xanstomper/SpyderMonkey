# Public share links: the unauthenticated data path AND a retention-expiry oracle

- source canon: `spydermonkey/engagement-ops.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

Players paste hand-share links on public forums (Reddit, 2+2, RUNitOnce) — every pasted link is a working UNAUTH data path and a timestamped probe:

1. **Harvest real share URLs from forums** (`web_search` for the share host + format fragments) to learn the platform's share formats — one estate serves several share TYPES (hand-replay, timeline, embedded image) with DIFFERENT id schemes AND lifetimes.
2. **Load one real link on the VM capturing every XHR** (puppeteer `page.on('response')`, filter `/api/`) — the SPA's own unauthenticated API calls fall out: the share resolver (`/api/share/alias?type=X&alias=Y`) and the data route behind it. The server-RENDERED `<title>` of a share page already leaks hand metadata (game, stakes, tournament id) to anyone — capture it as its own disclosure line.
3. **Decode the alias keyspace OFFLINE before touching the server again**: collect 5+ aliases, decode as base36/base62 big-ints, diff pairwise. Non-sequential magnitudes = random ~114-bit tokens = NOT enumerable — bank the negative row (share keys are strong) and stop mutating aliases; brute-forcing a proven-random keyspace wastes the noise budget.
4. **Re-fetch the OLDEST harvested aliases as the retention test**: a share that outlives the platform's own stated retention (docs claim 90-day downloads; a 4-year-old link still serving full hand data) = a DATA-class finding — permanent public hole-card/nickname exposure keyed by links the players themselves published. Compare share TYPES: some expired, some didn't = inconsistent-expiry discipline, part of the same row.
5. **Evidence even when bodies are encrypted**: (valid alias → 200 + payload size) vs (dead/mutated alias → small error envelope) is the validity oracle — the size delta works without decrypting anything.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
