# Next-session entry — chain composition

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-next-session-entry.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. Crash oracle (STILL OPEN, watcher armed): `~/holyshit-mode/scripts/sz_crash_watch.py` (stdlib, verified) rapid-polls `/public/gambling/crash` at 350ms once a game goes active — tests whether `crash_point_hundredths` arrives pre-crash. Game idle all session (`{"game":null}`). Run with `python3 -u` when piping output (banner buffering). Logs: `~/holyshit-mode/logs/crash_watch.log`.
2. `GET /public/cx-bucks/rewards` (amount/cooldown/gates) → single `POST /public/cx-bucks/claim` → balance delta. No claim-race probing.
3. If faucet accumulates: legit nuke purchase via checkout→launch (user asked for exactly this when funded). Nuke product UUID in `/tmp/prods.json` (regenerate from products route).
4. Watcher scripts: `sz_watch.py` (bg proc, GPS/hazard log) + `sz_tracker.py N` (foreground N-second picture) — both verified, run these before anything new.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
