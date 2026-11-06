# Ledger grammar (from this run) — mail / high-priv

- source canon: `holyshit-mode/llm-gateway-internal-control-plane.md`
- base technique: `holyshit-mode-llm-gateway-internal-control-plane-ledger-gram.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **mail** · auth **high-priv** · chain role **pivot**

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- `holyleadger chain` splits steps on the **unicode `→`**; keep the impact text free of arrows or
  you get 1 empty step. (Duplicated-chain files surfaced this run.)

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
