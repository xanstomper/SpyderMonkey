# Engagement-Artifact Sweep (the `git add -A` publication trap) — edge-node / high-priv

- source canon: `holyshit-mode/github-release-hygiene.md`
- base technique: `holyshit-mode-github-release-hygiene-engagement-artifact-swe.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **edge-node** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

`git add -A` in a repo with untracked engagement dirs (logs/, reports/, captures/) commits
and PUBLISHES them to the public mirror — an engagement report and a 10k-line watch log
landed in the HolyShit repo this way and had to be unpublished.

**Rule:** before any `git add -A`, run `git status --porcelain` and stage explicit paths
(scripts/, references/). `.gitignore` must carry `logs/`, `reports/`, `captures/`,
`__pycache__/`, `*.pyc` from day one.

**Unpublish ≠ purge:** `git rm --cached` + commit removes files from HEAD but they remain
in history — anyone can checkout the old commit. Full removal needs a force-push history
rewrite (operator's call; state it plainly when it happens).

## Probe adjustment (edge-node × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
