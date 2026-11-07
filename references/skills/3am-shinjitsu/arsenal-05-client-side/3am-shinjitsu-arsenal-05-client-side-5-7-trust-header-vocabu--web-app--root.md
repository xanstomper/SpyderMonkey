# 5.7 Trust-header vocabulary mining (score 70) — web-app / root

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- base technique: `3am-shinjitsu-arsenal-05-client-side-5-7-trust-header-vocabu.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- GREP chunks for `ssr-client-ip`, `x-client-geo`, `cf-ipcountry`, `country`, `region` header
  builders at call sites — SSR-to-API forwarding leaks the trust vocabulary.
- If the API honors client-supplied geo headers, region blocks (`451 er_sign_up_region_block`-
  class) are one header away. Spoof-test on the LEAST-throttled discriminating endpoint
  (game launch/demo), NEVER on the auth plane (self-DoS law, §3.7).

## Probe adjustment (web-app × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
