# Cloud Azure AD App Registration Overreach (CLOUD-AZ-03) — azure / machine

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-azure-ad-app-registration-ove.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **azure** · auth **machine** · chain role **pivot**

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- class: app registrations with excessive delegated/application grants
- probe: read-only grants inventory of the declared tenant
- wall: read-only

## Probe adjustment (azure × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
