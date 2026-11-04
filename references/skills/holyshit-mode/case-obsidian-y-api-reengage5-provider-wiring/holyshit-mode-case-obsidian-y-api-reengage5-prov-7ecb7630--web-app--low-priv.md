# Re-verification ladder (PTOK oracle first) — web-app / low-priv

- source canon: `holyshit-mode/case-obsidian-y-api-reengage5-provider-wiring.md`
- base technique: `holyshit-mode-case-obsidian-y-api-reengage5-provider-wiring-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **web-app** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Target live, `/pg/chat` still unauth on BOTH hosts (Render + Vercel), `/v1/models` 200.
- **ling model now STATELESS** (ptok 26 constant across 4 identical requests) — the shared
  cross-user buffer from re-engage #2 is GONE on ling at least. longcat ptok still varies
  (3148→3019) but that's the live-timestamp in its injected Environment, not shared context.
  Prior score-85 shared-context + score-95 poisoning findings should be treated as LIKELY
  PATCHED until a fresh drift test proves otherwise. Finding decay confirmed empirically.

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
