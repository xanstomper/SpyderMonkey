# 7. The same feed leaks privacy-opted users — iot-edge / guest

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-7-the-same-feed-lea.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **iot-edge** · auth **guest** · chain role **pivot**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

Game feeds commonly ship hidden_mode users with the name masked but the internal
userId, xp, and per-play walletInfo INTACT — including the live balance draining bet by
bet (real units, e.g. SOL_LAMPORT). That is real-time financial surveillance of
privacy-opted users by anyone with a websocket; it is usually the third leak path after
the lobby firehose (leaderboards/bigwins) and game-detail rows. Fix to state: strip
id/xp/balance server-side on every feed path when hidden_mode is set — never rely on
UI masking.

## Probe adjustment (iot-edge × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
