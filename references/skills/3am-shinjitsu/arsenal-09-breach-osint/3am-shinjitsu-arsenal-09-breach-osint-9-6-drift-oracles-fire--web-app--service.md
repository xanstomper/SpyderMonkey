# 9.6 Drift oracles — fire FIRST on every re-entry (score 90, mandatory) — web-app / service

- source canon: `3am-shinjitsu/arsenal-09-breach-osint.md`
- base technique: `3am-shinjitsu-arsenal-09-breach-osint-9-6-drift-oracles-fire.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **web-app** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- PTOK drift (LLM targets): 3× identical 1-word requests → `usage.prompt_tokens`: constant =
  stateless/patched; drifting = shared buffer re-emerged (highest-value re-find).
- Bundle-hash diff (§2.8), wayback CDX diff (§2.3), wall-shape re-verify (403 → 500 drift).
- TOP prior compromisables were patched between sessions — re-asserting without a fresh test
  is a stale-finding ERROR.

## Probe adjustment (web-app × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
