# 7. The same feed leaks privacy-opted users — api / low-priv

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-7-the-same-feed-lea.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **api** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Game feeds commonly ship hidden_mode users with the name masked but the internal
userId, xp, and per-play walletInfo INTACT — including the live balance draining bet by
bet (real units, e.g. SOL_LAMPORT). That is real-time financial surveillance of
privacy-opted users by anyone with a websocket; it is usually the third leak path after
the lobby firehose (leaderboards/bigwins) and game-detail rows. Fix to state: strip
id/xp/balance server-side on every feed path when hidden_mode is set — never rely on
UI masking.

## Probe adjustment (api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
