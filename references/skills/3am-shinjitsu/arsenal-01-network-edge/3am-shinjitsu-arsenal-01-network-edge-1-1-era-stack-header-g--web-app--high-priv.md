# 1.1 Era-stack header grab (score 80, T≈1min) — web-app / high-priv

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-1-era-stack-header-g.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **high-priv** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- DECISIVE: `curl -sI https://<target>/` and on the API host separately
- READ: `Server`, `X-Powered-By`, `via`, `x-served-by`, `x-turbo-by`, `x-kong-*`,
  `www-authenticate`, `content-generator`, `x-generator`
- CONFIRMED WHEN: any component EOL per §1.12 table
- FP: CDN-injected headers (`via` from CF/Fastly is not the origin stack)

## Probe adjustment (web-app × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
