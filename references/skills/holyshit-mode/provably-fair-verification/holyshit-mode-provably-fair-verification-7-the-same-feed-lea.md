# 7. The same feed leaks privacy-opted users

- source canon: `holyshit-mode/provably-fair-verification.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Game feeds commonly ship hidden_mode users with the name masked but the internal
userId, xp, and per-play walletInfo INTACT — including the live balance draining bet by
bet (real units, e.g. SOL_LAMPORT). That is real-time financial surveillance of
privacy-opted users by anyone with a websocket; it is usually the third leak path after
the lobby firehose (leaderboards/bigwins) and game-detail rows. Fix to state: strip
id/xp/balance server-side on every feed path when hidden_mode is set — never rely on
UI masking.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
