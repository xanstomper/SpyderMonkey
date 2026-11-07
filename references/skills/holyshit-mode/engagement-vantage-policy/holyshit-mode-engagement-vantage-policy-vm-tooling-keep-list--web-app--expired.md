# VM tooling (keep list current) — web-app / expired

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- base technique: `holyshit-mode-engagement-vantage-policy-vm-tooling-keep-list.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **web-app** · auth **expired** · chain role **pivot**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

python3.9, curl, dig, openssl, jq, nc/ncat, whois, nmap. OL9 = dnf; sudo -n works.
Recon kit added since: `curl-impersonate-chrome` in `~/dkv-venv/bin` (JA3 bypass, see
TLS-impersonation section), chromium-browser + Xvfb (`DISPLAY=:99`, CDP `127.0.0.1:9222`,
profile `/tmp/chrome-prof`) for real-browser surfaces, user-level pip packages in
`~/dkv-venv` (websocket-client, msgpack, eth-account, python-socketio, requests). Kill
chromium with `pkill -9 chromium` and relaunch fresh with `--no-sandbox` + a new
`--user-data-dir` when it gets stuck in an existing-session loop.

## Probe adjustment (web-app × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
