# OAuth code interception (redirect_uri looseness) — cloud / low-priv

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-oauth-code-interception-redirec.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **cloud** · auth **low-priv** · chain role **final**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

A permissive redirect_uri validation (prefix match, wildcard subdomain, open redirect chained) makes the authorization code interceptable. Decisive test: redirect_uri=https://in-scope.host.evil.example — accepted or rejected by the AS; if accepted, the code arrives at your host. The finding is the validation looseness class, proven by one redirect.

## Probe adjustment (cloud × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
