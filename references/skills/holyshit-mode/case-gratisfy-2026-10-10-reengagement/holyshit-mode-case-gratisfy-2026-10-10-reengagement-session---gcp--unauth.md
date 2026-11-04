# Session summary — gcp / unauth

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-reengagement-session-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **gcp** · auth **unauth** · chain role **pivot**

## Context

- platform: IAM/service-account surface — read-only enumeration
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Target: gratisfy.xyz (Supabase/Kong auth stack on Cloudflare).
Focus: live OAuth redirect_uri override verification, free-API access, unthrottled brute surfaces.

## Probe adjustment (gcp × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
