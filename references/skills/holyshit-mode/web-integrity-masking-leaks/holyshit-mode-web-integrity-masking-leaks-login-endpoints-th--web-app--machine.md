# Login endpoints that mint on any input — web-app / machine

- source canon: `holyshit-mode/web-integrity-masking-leaks.md`
- base technique: `holyshit-mode-web-integrity-masking-leaks-login-endpoints-th.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **machine** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

An API login returning `200 + token + config` for wrong passwords AND
nonexistent users is an UNCONDITIONAL SESSION MINT (an auth-design flaw worth
logging) — it is NOT access.

Discriminator (burned once by a false positive — four "default creds work!"
reports were all the anon shell):

- Compare wrong-password vs nonexistent-user responses FIELD-BY-FIELD.
- Populated `error` field + empty user/panel keys = mint-with-failed-auth.
- Only a real credential pair yielding a POPULATED user/panel = access.
- A naive "response contains token+panel" check false-positives.

## Probe adjustment (web-app × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
