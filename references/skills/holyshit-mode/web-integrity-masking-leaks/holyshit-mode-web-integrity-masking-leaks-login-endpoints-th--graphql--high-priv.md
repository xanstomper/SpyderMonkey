# Login endpoints that mint on any input — graphql / high-priv

- source canon: `holyshit-mode/web-integrity-masking-leaks.md`
- base technique: `holyshit-mode-web-integrity-masking-leaks-login-endpoints-th.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **graphql** · auth **high-priv** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (graphql × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
