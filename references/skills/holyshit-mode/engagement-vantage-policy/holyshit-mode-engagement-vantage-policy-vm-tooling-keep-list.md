# VM tooling (keep list current)

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

python3.9, curl, dig, openssl, jq, nc/ncat, whois, nmap. OL9 = dnf; sudo -n works.
Recon kit added since: `curl-impersonate-chrome` in `~/dkv-venv/bin` (JA3 bypass, see
TLS-impersonation section), chromium-browser + Xvfb (`DISPLAY=:99`, CDP `127.0.0.1:9222`,
profile `/tmp/chrome-prof`) for real-browser surfaces, user-level pip packages in
`~/dkv-venv` (websocket-client, msgpack, eth-account, python-socketio, requests). Kill
chromium with `pkill -9 chromium` and relaunch fresh with `--no-sandbox` + a new
`--user-data-dir` when it gets stuck in an existing-session loop.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
