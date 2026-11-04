# 3.5 PostgREST error oracles (score 70, RLS-safe recon) — websocket / unauth

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-5-postgrest-error-oracles-sco.md`
- bindings: **WSTG-SESS-01** · **CWE-347** · **ATT&CK T1552**
- context: **websocket** · auth **unauth** · chain role **entry**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- `PGRST205` table absent · `[]` table exists+RLS-gated · `42703` on `?select=<col>` = free
  column-name brute · `22P02` = column TYPE oracle · `PGRST301` = PostgREST uses a DIFFERENT
  JWT trust root than GoTrue (forge against both separately).
- Schema map from errors = coverage finding even when RLS holds.

## Probe adjustment (websocket × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
