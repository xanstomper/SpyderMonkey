# The `.pyc` Leak — worker / service

- source canon: `holyshit-mode/github-release-hygiene.md`
- base technique: `holyshit-mode-github-release-hygiene-the-pyc-leak.md`
- bindings: **WSTG-CONF-04** · **CWE-538** · **ATT&CK T1552**
- context: **worker** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

`git add -A` silently commits `__pycache__/*.pyc` after any local run. The first release
of holyshit-mode shipped a `.pyc` before `.gitignore` existed; it was caught only because
`git ls-files` was manually checked post-push.

**Rule:** create `.gitignore` with `__pycache__/` + `*.pyc` BEFORE the first `git commit`.
If already committed: `git rm -r --cached scripts/__pycache__` then commit + push.

## Probe adjustment (worker × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
