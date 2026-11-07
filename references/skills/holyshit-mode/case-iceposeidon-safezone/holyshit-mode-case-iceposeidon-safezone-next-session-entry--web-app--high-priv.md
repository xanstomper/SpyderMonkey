# Next-session entry — web-app / high-priv

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-next-session-entry.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **web-app** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

1. Crash oracle (STILL OPEN, watcher armed): `~/holyshit-mode/scripts/sz_crash_watch.py` (stdlib, verified) rapid-polls `/public/gambling/crash` at 350ms once a game goes active — tests whether `crash_point_hundredths` arrives pre-crash. Game idle all session (`{"game":null}`). Run with `python3 -u` when piping output (banner buffering). Logs: `~/holyshit-mode/logs/crash_watch.log`.
2. `GET /public/cx-bucks/rewards` (amount/cooldown/gates) → single `POST /public/cx-bucks/claim` → balance delta. No claim-race probing.
3. If faucet accumulates: legit nuke purchase via checkout→launch (user asked for exactly this when funded). Nuke product UUID in `/tmp/prods.json` (regenerate from products route).
4. Watcher scripts: `sz_watch.py` (bg proc, GPS/hazard log) + `sz_tracker.py N` (foreground N-second picture) — both verified, run these before anything new.

## Probe adjustment (web-app × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
