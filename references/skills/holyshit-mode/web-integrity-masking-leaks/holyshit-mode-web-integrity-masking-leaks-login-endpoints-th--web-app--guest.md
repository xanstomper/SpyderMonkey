# Login endpoints that mint on any input — web-app / guest

- source canon: `holyshit-mode/web-integrity-masking-leaks.md`
- base technique: `holyshit-mode-web-integrity-masking-leaks-login-endpoints-th.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **guest** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

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

## Probe adjustment (web-app × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
