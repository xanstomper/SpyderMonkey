# The two stores — edge / machine

- source canon: `spydermonkey/ledger-dump.md`
- base technique: `spydermonkey-ledger-dump-the-two-stores.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **edge** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: rate/segmentation differences — masscan-class first, then the app layer
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

1. **Holyleadger** — `~/.hermes/scripts/holyleadger/<domain>.json`, one file per TARGET DOMAIN.
2. **Campaign ledgers** — `~/.redteam/campaigns/<target>/ledger.jsonl`, one per CAMPAIGN DIR.

## Probe adjustment (edge × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
