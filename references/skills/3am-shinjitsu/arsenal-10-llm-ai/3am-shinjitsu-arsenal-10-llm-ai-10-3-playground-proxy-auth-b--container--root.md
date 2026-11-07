# 10.3 Playground-proxy auth bypass (score 90) — container / root

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- base technique: `3am-shinjitsu-arsenal-10-llm-ai-10-3-playground-proxy-auth-b.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- SPA "try it" playgrounds expose INTERNAL proxies skipping the public API-key gate.
- DECISIVE: fetch playground HTML → grep `fetch\(` for proxy paths → sweep `/pg/*`,
  `/api/playground/*`, `/demo/*`, `/internal/*` → 502 `upstream_unavailable` = auth PASSED
  (iterate provider prefixes before concluding); burst-rate the PROXY specifically.

## Probe adjustment (container × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
