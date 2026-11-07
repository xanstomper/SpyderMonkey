# Next-session entry

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

1. Crash oracle (STILL OPEN, watcher armed): `~/holyshit-mode/scripts/sz_crash_watch.py` (stdlib, verified) rapid-polls `/public/gambling/crash` at 350ms once a game goes active — tests whether `crash_point_hundredths` arrives pre-crash. Game idle all session (`{"game":null}`). Run with `python3 -u` when piping output (banner buffering). Logs: `~/holyshit-mode/logs/crash_watch.log`.
2. `GET /public/cx-bucks/rewards` (amount/cooldown/gates) → single `POST /public/cx-bucks/claim` → balance delta. No claim-race probing.
3. If faucet accumulates: legit nuke purchase via checkout→launch (user asked for exactly this when funded). Nuke product UUID in `/tmp/prods.json` (regenerate from products route).
4. Watcher scripts: `sz_watch.py` (bg proc, GPS/hazard log) + `sz_tracker.py N` (foreground N-second picture) — both verified, run these before anything new.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
