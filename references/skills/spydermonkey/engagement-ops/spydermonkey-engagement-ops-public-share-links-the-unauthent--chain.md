# Public share links: the unauthenticated data path AND a retention-expiry oracle — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-public-share-links-the-unauthent.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Players paste hand-share links on public forums (Reddit, 2+2, RUNitOnce) — every pasted link is a working UNAUTH data path and a timestamped probe:

1. **Harvest real share URLs from forums** (`web_search` for the share host + format fragments) to learn the platform's share formats — one estate serves several share TYPES (hand-replay, timeline, embedded image) with DIFFERENT id schemes AND lifetimes.
2. **Load one real link on the VM capturing every XHR** (puppeteer `page.on('response')`, filter `/api/`) — the SPA's own unauthenticated API calls fall out: the share resolver (`/api/share/alias?type=X&alias=Y`) and the data route behind it. The server-RENDERED `<title>` of a share page already leaks hand metadata (game, stakes, tournament id) to anyone — capture it as its own disclosure line.
3. **Decode the alias keyspace OFFLINE before touching the server again**: collect 5+ aliases, decode as base36/base62 big-ints, diff pairwise. Non-sequential magnitudes = random ~114-bit tokens = NOT enumerable — bank the negative row (share keys are strong) and stop mutating aliases; brute-forcing a proven-random keyspace wastes the noise budget.
4. **Re-fetch the OLDEST harvested aliases as the retention test**: a share that outlives the platform's own stated retention (docs claim 90-day downloads; a 4-year-old link still serving full hand data) = a DATA-class finding — permanent public hole-card/nickname exposure keyed by links the players themselves published. Compare share TYPES: some expired, some didn't = inconsistent-expiry discipline, part of the same row.
5. **Evidence even when bodies are encrypted**: (valid alias → 200 + payload size) vs (dead/mutated alias → small error envelope) is the validity oracle — the size delta works without decrypting anything.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
