# T+40 — decision point — ci-cd / high-priv

- source canon: `3am-shinjitsu/arsenal-index.md`
- base technique: `3am-shinjitsu-arsenal-index-t-40-decision-point.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **ci-cd** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Every probe above → ledger entry (`campaign-state.json`). Re-score. Remaining time goes to
the highest-Score' hypothesis from `arsenal-03` (API) and `arsenal-04` (auth), NOT to
wordlist spraying. Exhausted class = N/A'd with the exact test string, never re-probed.

## Probe adjustment (ci-cd × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
