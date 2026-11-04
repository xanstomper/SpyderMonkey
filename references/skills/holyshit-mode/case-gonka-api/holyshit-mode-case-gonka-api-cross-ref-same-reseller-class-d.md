# Cross-ref: same reseller class, different stack (apimart.ai, 2026-10-06)

- source canon: `holyshit-mode/case-gonka-api.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

apimart.ai = the OneAPI/new-api variant of the sketchy-reseller class (SEO-spam
botnet on GitHub, `x-oneapi-request-id` fingerprint, 309 models). Full recipe +
route-mining method: `references/case-apimart-newapi-fork.md`. Use both files
together when engaging this class — Supabase/Lovable stack vs Go/OneAPI fork
have different recon ladders (chunk-mining + upstream-source reading vs
PostgREST oracles).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
