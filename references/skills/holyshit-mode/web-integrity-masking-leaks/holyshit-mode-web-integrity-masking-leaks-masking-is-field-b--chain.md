# Masking is field-by-field — enumerate ALIAS fields — chain composition

- source canon: `holyshit-mode/web-integrity-masking-leaks.md`
- base technique: `holyshit-mode-web-integrity-masking-leaks-masking-is-field-b.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

A server that masks `username` for privacy-opted users routinely ships
`display_username` (or avatar URLs, steam/oauth links, referral handles) with the
REAL identity verbatim. Never conclude "masking works" from the primary field.

Method:
1. Capture the feed (socket firehose, leaderboard events, bet streams).
2. Regex every user-object shape:
   `set(tuple(sorted(set(re.findall(r'"([a-z_]{3,30})":', obj)))))` over
   `\{"id":\d+,...\}` matches.
3. Diff the shapes: which ones carry identity fields for masked users?
   On gamdom: 197/200 leaderboard rows leaked real names via `display_username`
   while 1,300+ bet-feed rows masked correctly (but still shipped IDs + live
   wallet balances in real units).

Report the leak PER PATH with row counts, not as one blob — the fix is
path-local (NULL the alias field on the one leaking path).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
