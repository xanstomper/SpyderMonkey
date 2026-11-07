# 7.5 Registry/CI secret exposure (score 85 when found)

- source canon: `3am-shinjitsu/arsenal-07-supply-chain.md`
- bindings: **WSTG-SESS-01** · **CWE-347** · **ATT&CK T1552**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Public repo/paste scan of org namespace for keys (`sk_`, `eyJ` JWT shapes, `AKIA`),
  workflow logs, committed `.env` history (git log on public clones).
- A leaked key = a FINDING, not a license: one read-only privilege confirmation (`/v1/credits`
  class balance endpoint), then documentation (§2 scope gate).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
