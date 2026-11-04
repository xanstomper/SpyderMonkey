# Chain certification (state + report) — api / unauth

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-chain-certification-state-r.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **api** · auth **unauth** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Campaign state `chains[]`: `{crown_jewel, steps, status, impact, evidence}`.
- `steps` written as `A→B→C` where each hop is a confirmed primitive.
- `status: TAKEOVER` only when the final hop's decisive proof LANDED.
- `status: PARTIAL` = primitive confirmed but the impact-gate is missing — name it.
- `status: BLOCKED` = the deck stops here (auth, vantage, wall) — name the exact gap.
Tooling: `python3 scripts/exploit-intel.py chain --target <t> --jewel <crown> \
--steps "A→B→C:TAKEOVER" --impact "<one line>"` — dedupes, renders in `report`.

## Probe adjustment (api × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
