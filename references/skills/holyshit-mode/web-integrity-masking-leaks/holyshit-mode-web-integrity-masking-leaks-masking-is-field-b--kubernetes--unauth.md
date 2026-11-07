# Masking is field-by-field — enumerate ALIAS fields — kubernetes / unauth

- source canon: `holyshit-mode/web-integrity-masking-leaks.md`
- base technique: `holyshit-mode-web-integrity-masking-leaks-masking-is-field-b.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **kubernetes** · auth **unauth** · chain role **entry**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

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

## Probe adjustment (kubernetes × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
