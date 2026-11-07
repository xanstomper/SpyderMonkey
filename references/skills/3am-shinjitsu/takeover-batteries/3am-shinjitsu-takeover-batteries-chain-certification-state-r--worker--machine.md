# Chain certification (state + report) — worker / machine

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-chain-certification-state-r.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **worker** · auth **machine** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Campaign state `chains[]`: `{crown_jewel, steps, status, impact, evidence}`.
- `steps` written as `A→B→C` where each hop is a confirmed primitive.
- `status: TAKEOVER` only when the final hop's decisive proof LANDED.
- `status: PARTIAL` = primitive confirmed but the impact-gate is missing — name it.
- `status: BLOCKED` = the deck stops here (auth, vantage, wall) — name the exact gap.
Tooling: `python3 scripts/exploit-intel.py chain --target <t> --jewel <crown> \
--steps "A→B→C:TAKEOVER" --impact "<one line>"` — dedupes, renders in `report`.

## Probe adjustment (worker × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
