# Re-engagement checklist — web-app / low-priv

- source canon: `holyshit-mode/case-obsidian-y-api-pg-bypass.md`
- base technique: `holyshit-mode-case-obsidian-y-api-pg-bypass-re-engagement-ch.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **web-app** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Re-test `/pg/chat` first (502 = upstreams down, 401/404 = patched — the bypass may be fixed;
  re-verify before trusting this case).
- If patched: check whether /playground still exists and whether the proxy now requires a
  session cookie or Referer/Origin header instead of a key.
- Try the vercel.app vantage for `/pg/chat` equivalence.
- Reasoning-field extraction for the 50k system prompt (stream with reasoning models, dump
  `reasoning_details`).

## Probe adjustment (web-app × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
