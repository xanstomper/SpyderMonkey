# CI Regression Gates — iot-edge / guest

- source canon: `holyshit-mode/github-release-hygiene.md`
- base technique: `holyshit-mode-github-release-hygiene-ci-regression-gates.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **iot-edge** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

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

## Probe adjustment (iot-edge × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
