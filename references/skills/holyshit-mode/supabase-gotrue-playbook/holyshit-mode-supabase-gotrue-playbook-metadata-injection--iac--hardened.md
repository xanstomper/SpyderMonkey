# Metadata injection — iac / hardened

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- base technique: `holyshit-mode-supabase-gotrue-playbook-metadata-injection.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iac** · auth **hardened** · chain role **pivot**

## Context

- platform: template/state files are the infrastructure inventory — read-only crown of the exposure
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

`user_metadata.role=admin`, `credits:999999` persists into the JWT (GoTrue does not strip user_metadata). But backends authorize on their own DB (profiles table / app_metadata), so admin claims almost never escalate. Record persistence as confirmed; expect authorization to fail.

## Probe adjustment (iac × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
