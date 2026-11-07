# CI Regression Gates — gateway / high-priv

- source canon: `holyshit-mode/github-release-hygiene.md`
- base technique: `holyshit-mode-github-release-hygiene-ci-regression-gates.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **gateway** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Manual "did I truncate the file?" checks don't scale. The verify.yml workflow runs on
every push:

```yaml
- name: Validate README line counts
  run: |
    MANDATE_LINES=$(wc -l < references/mandate.txt)
    MATRIX_CLASSES=$(grep -c "^- " references/vector-matrix.md)
    if [ "$MANDATE_LINES" -lt 100 ]; then exit 1; fi
    if [ "$MATRIX_CLASSES" -lt 100 ]; then exit 1; fi
```

Any accidental truncation of a large reference file fails CI before the operator notices.

## Probe adjustment (gateway × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
