# Vendor SDK supply-chain (the SPY-095 class family)

- source canon: `spydermonkey/technique-canon-5.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

Production pages importing personal/third-party infra (workers.dev class), SDK env-defaults (`mode||"development"`), auth material in URLs. Decisive test: passive capture of the page's OWN traffic (in-scope), the executing SDK pulled and cold-mapped — the env->host map verbatim is the crown.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
