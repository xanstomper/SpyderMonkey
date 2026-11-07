# 1.11 Request-smuggling differential (score 55) [owned infra only] — edge / machine

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-11-request-smuggling.md`
- bindings: **WSTG-ADV-02** · **CWE-444** · **ATT&CK T1190**
- context: **edge** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: rate/segmentation differences — masscan-class first, then the app layer
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- ONE CL.TE differential probe max; timing-only. Any ambiguity = stop, document, never iterate.
- Serverless/CDN-fronted (no dual proxy layer) = N/A — say once, pivot.

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
