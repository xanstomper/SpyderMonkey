# Secret Scan in CI — ci-cd / low-priv

- source canon: `holyshit-mode/github-release-hygiene.md`
- base technique: `holyshit-mode-github-release-hygiene-secret-scan-in-ci.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **ci-cd** · auth **low-priv** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

The workflow greps for `sk-[a-z0-9]{20,}`, `gho_[a-z0-9]{20,}`, `api_key = '<20+ chars>'`,
`Bearer <20+ chars>` on every push. Exclusions: `.env.example` (placeholder values only)
and env-var NAMES like `HOLYSHIT_API_KEY` (no value).

**Rule:** never put real key material in any repo file, even "temporarily". CI catches it.

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
