# Score: 92 (High) — ci-cd / low-priv

- source canon: `holyshit-mode/case-freeinference-org.md`
- base technique: `holyshit-mode-case-freeinference-org-score-92-high.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- context: **ci-cd** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- **E** (Exploitability): 9 — trivial wordlist brute, no tooling required
- **I** (Impact): 9 — full infra topology + live utilization + traffic volumes
- **L** (Likelihood): 8 — password `madsys` found on 7th attempt; real password likely equally weak
- **R** (Reproducibility): 9 — single curl with correct password returns 6.3MB
- **N** (Novelty): 7 — shared-secret telemetry endpoint is a distinct pattern, but brute-without-rate-limit is classic OWASP

## Probe adjustment (ci-cd × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
