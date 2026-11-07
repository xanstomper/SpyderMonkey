# Post-Push Verification Checklist — websocket / machine

- source canon: `holyshit-mode/github-release-hygiene.md`
- base technique: `holyshit-mode-github-release-hygiene-post-push-verification-.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **websocket** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

1. `git ls-files | sort` — confirm no `.pyc`, `.env`, or unexpected files
2. `curl https://raw.githubusercontent.com/<org>/<repo>/main/README.md | head -5` —
   confirm README renders on the default branch
3. `gh api repos/<org>/<repo>/actions/runs?per_page=1` — confirm latest run conclusion=success
4. Leak scan: `grep -rniE "sk-[a-z0-9]{20,}|gho_[a-z0-9]{20,}|bearer [a-z0-9]{20,}" .`
   (excluding `.env.example` and env-var names)

## Probe adjustment (websocket × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
