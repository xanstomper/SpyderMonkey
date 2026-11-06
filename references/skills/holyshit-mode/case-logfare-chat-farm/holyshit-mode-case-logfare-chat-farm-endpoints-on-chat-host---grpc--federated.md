# Endpoints on chat host (all Origin-gated, all real JSON) — grpc / federated

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-endpoints-on-chat-host-.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **grpc** · auth **federated** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

`/api/health {status,version}` · `/api/models` (full tier/visibility/premium intel; leaks hidden default `claude-sonnet-4.5` not in public list) · `/api/chat` · `/api/conversations` (GET list / PATCH / DELETE per-id) · `/api/settings` (GET/PUT) · `/api/consent` (GET: `{tier:"anonymous",can_use_premium:false,logged_in:false}`).

## Probe adjustment (grpc × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
