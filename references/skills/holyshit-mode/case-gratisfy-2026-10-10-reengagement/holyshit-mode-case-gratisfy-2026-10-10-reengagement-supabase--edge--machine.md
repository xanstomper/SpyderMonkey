# Supabase anon key — TRUNCATED placeholder — edge / machine

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-reengagement-supabase.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- context: **edge** · auth **machine** · chain role **pivot**

## Context

- platform: rate/segmentation differences — masscan-class first, then the app layer
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

VITE_SUPABASE_ANON_KEY in bundle is truncated (eyJhbG...YuCQ). Full key via curl with browser-spoof headers.

## Probe adjustment (edge × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
