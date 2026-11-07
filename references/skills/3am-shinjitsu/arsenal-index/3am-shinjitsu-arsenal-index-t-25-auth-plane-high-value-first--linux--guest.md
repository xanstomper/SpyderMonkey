# T+25 — auth plane (high-value first, ceiling 15 req) — linux / guest

- source canon: `3am-shinjitsu/arsenal-index.md`
- base technique: `3am-shinjitsu-arsenal-index-t-25-auth-plane-high-value-first.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **linux** · auth **guest** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

| # | Probe | Test | Confirmed-when |
|---|---|---|---|
| 22 | GoTrue settings | `curl -H 'apikey: <anon>' /auth/v1/settings /auth/v1/health` | providers, autoconfirm flags, version = full auth surface |
| 23 | OAuth state binding | 2× /start → state A,B; `callback?state=A&code=fake` with cookie B | `Invalid OAuth state` = hardened (negative, ledger it) |
| 24 | redirect_uri override | `curl -s -o /dev/null -w '%{redirect_url}' '/auth/v1/authorize?provider=discord&redirect_uri=https://evil.com/cb'` | Location carries attacker URI verbatim → live-intercept (`arsenal-04` §3.2) |
| 25 | Auth-chain rate sweep | 15-20 rapid garbage POSTs per auth endpoint, `-w '%{http_code}'` | zero 429 = brute surface open |
| 26 | WS handshake+frames | real frame exchange (socket+ssl), NOT curl 101 | CLOSE 1008 on first frame = gate works (negative) |

## Probe adjustment (linux × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
