# Pairs with `next` — mail / machine

- source canon: `holyshit-mode/engagement-report-pattern.md`
- base technique: `holyshit-mode-engagement-report-pattern-pairs-with-next.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **mail** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

`holyleadger.py next --top N` is the inverse view: it lists the highest-value ACTIONS
(re-verify decayed confirmed, prove hypotheses, re-probe crown paths) and excludes
negatives. `report` shows "here's what we found"; `next` shows "here's what to do next."
Operators run `next`, execute the top `holyshit scan <task>` commands, then `report` to see the ledger consolidate.

## Probe adjustment (mail × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
