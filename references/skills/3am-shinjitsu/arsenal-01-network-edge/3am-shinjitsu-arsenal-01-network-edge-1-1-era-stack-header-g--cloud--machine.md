# 1.1 Era-stack header grab (score 80, T≈1min) — cloud / machine

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-1-era-stack-header-g.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **cloud** · auth **machine** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- DECISIVE: `curl -sI https://<target>/` and on the API host separately
- READ: `Server`, `X-Powered-By`, `via`, `x-served-by`, `x-turbo-by`, `x-kong-*`,
  `www-authenticate`, `content-generator`, `x-generator`
- CONFIRMED WHEN: any component EOL per §1.12 table
- FP: CDN-injected headers (`via` from CF/Fastly is not the origin stack)

## Probe adjustment (cloud × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
