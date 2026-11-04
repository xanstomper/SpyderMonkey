# The `.pyc` Leak

- source canon: `holyshit-mode/github-release-hygiene.md`
- bindings: **WSTG-CONF-04** · **CWE-538** · **ATT&CK T1552**
- generated: 2026-11-04

## The technique

`git add -A` silently commits `__pycache__/*.pyc` after any local run. The first release
of holyshit-mode shipped a `.pyc` before `.gitignore` existed; it was caught only because
`git ls-files` was manually checked post-push.

**Rule:** create `.gitignore` with `__pycache__/` + `*.pyc` BEFORE the first `git commit`.
If already committed: `git rm -r --cached scripts/__pycache__` then commit + push.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
