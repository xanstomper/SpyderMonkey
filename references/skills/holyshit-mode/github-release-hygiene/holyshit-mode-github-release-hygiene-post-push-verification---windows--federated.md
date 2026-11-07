# Post-Push Verification Checklist — windows / federated

- source canon: `holyshit-mode/github-release-hygiene.md`
- base technique: `holyshit-mode-github-release-hygiene-post-push-verification-.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **windows** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

1. `git ls-files | sort` — confirm no `.pyc`, `.env`, or unexpected files
2. `curl https://raw.githubusercontent.com/<org>/<repo>/main/README.md | head -5` —
   confirm README renders on the default branch
3. `gh api repos/<org>/<repo>/actions/runs?per_page=1` — confirm latest run conclusion=success
4. Leak scan: `grep -rniE "sk-[a-z0-9]{20,}|gho_[a-z0-9]{20,}|bearer [a-z0-9]{20,}" .`
   (excluding `.env.example` and env-var names)

## Probe adjustment (windows × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
