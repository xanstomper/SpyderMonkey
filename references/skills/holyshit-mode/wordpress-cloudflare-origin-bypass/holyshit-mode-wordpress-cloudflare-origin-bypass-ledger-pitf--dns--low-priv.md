# Ledger pitfalls — dns / low-priv

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-ledger-pitf.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **dns** · auth **low-priv** · chain role **pivot**

## Context

- platform: record/cname surface — the domtake chain starts here
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- `holyleadger chain` splits the chain value on `-->`. If you embed `->` in the `--impact` text,
  the chain parser fragment and you get "1 step". Keep `--impact` free of arrow sequences.
- Statuses are lowercase (`confirmed|negative|hypothesis`). Set `HOLYSHIT_TARGET=<domain>` or pass
  `--target` or every `add` fails.

## Probe adjustment (dns × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
