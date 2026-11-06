# Re-engagement checklist — mobile-api / high-priv

- source canon: `holyshit-mode/case-obsidian-y-api-pg-bypass.md`
- base technique: `holyshit-mode-case-obsidian-y-api-pg-bypass-re-engagement-ch.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **mobile-api** · auth **high-priv** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Re-test `/pg/chat` first (502 = upstreams down, 401/404 = patched — the bypass may be fixed;
  re-verify before trusting this case).
- If patched: check whether /playground still exists and whether the proxy now requires a
  session cookie or Referer/Origin header instead of a key.
- Try the vercel.app vantage for `/pg/chat` equivalence.
- Reasoning-field extraction for the 50k system prompt (stream with reasoning models, dump
  `reasoning_details`).

## Probe adjustment (mobile-api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
