# The two stores — mail / high-priv

- source canon: `spydermonkey/ledger-dump.md`
- base technique: `spydermonkey-ledger-dump-the-two-stores.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **mail** · auth **high-priv** · chain role **pivot**

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

1. **Holyleadger** — `~/.hermes/scripts/holyleadger/<domain>.json`, one file per TARGET DOMAIN.
2. **Campaign ledgers** — `~/.redteam/campaigns/<target>/ledger.jsonl`, one per CAMPAIGN DIR.

## Probe adjustment (mail × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
