# Not every publicly-pushed value is a leak — api / high-priv

- source canon: `holyshit-mode/web-integrity-masking-leaks.md`
- base technique: `holyshit-mode-web-integrity-masking-leaks-not-every-publicly.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **api** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

A "next round" field can be the REFERENCE state the game publishes for gameplay:
hilo announces `apriori: {color, number}` = the CURRENT card players bet
higher/lower against (public BY DESIGN). Check the game rules before reporting
an outcome leak — the genuinely hidden value arrives only in an authed event.

## Probe adjustment (api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
