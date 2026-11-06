# Cross-ref: same reseller class, different stack (apimart.ai, 2026-10-06) — container / low-priv

- source canon: `holyshit-mode/case-gonka-api.md`
- base technique: `holyshit-mode-case-gonka-api-cross-ref-same-reseller-class-d.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **container** · auth **low-priv** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

apimart.ai = the OneAPI/new-api variant of the sketchy-reseller class (SEO-spam
botnet on GitHub, `x-oneapi-request-id` fingerprint, 309 models). Full recipe +
route-mining method: `references/case-apimart-newapi-fork.md`. Use both files
together when engaging this class — Supabase/Lovable stack vs Go/OneAPI fork
have different recon ladders (chunk-mining + upstream-source reading vs
PostgREST oracles).

## Probe adjustment (container × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
