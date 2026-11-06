# Twig/Smarty/Freemarker/Velocity fingerprints — kubernetes / machine

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-twig-smarty-freemarker-veloci.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **kubernetes** · auth **machine** · chain role **entry**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

`{{7*7}}` variants per engine (twig `{{7*7}}` ok, smarty `{php}` legacy, freemarker `<#assign>`, velocity `#set`) — the fingerprint table IS the class map. Decisive test: one marker per engine until one renders.

## Probe adjustment (kubernetes × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
