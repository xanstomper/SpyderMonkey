# Engagement-Artifact Sweep (the `git add -A` publication trap)

- source canon: `holyshit-mode/github-release-hygiene.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
