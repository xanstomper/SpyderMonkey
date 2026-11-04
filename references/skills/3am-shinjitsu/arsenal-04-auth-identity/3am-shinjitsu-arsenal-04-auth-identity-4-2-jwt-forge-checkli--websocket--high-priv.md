# 4.2 JWT forge checklist — OFFLINE FIRST (zero traffic before this) — websocket / high-priv

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- base technique: `3am-shinjitsu-arsenal-04-auth-identity-4-2-jwt-forge-checkli.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **high-priv** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- (a) OFFLINE crack of known sig with default/self-hosted secrets (SupaBomb list) — hashcat.
- (b) HS256 forge with anon-key-as-secret against `/auth/v1/user` AND `/rest/v1/` separately
  (`PGRST301` = separate trust root).
- (c) alg:none, `jwk` header injection, tamper-keep-sig, kid-injection, RS256→HS256 confusion.
- GoTrue checks claims BEFORE signature: `missing sub claim` = sig never ran — reorder probes.
- Uniform `invalid_api_key` for EVERY bearer/JWT/alg-none variant = no JWT path exists —
  log the negative, STOP (keys are opaque strings; forging is chasing nothing).

## Probe adjustment (websocket × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
