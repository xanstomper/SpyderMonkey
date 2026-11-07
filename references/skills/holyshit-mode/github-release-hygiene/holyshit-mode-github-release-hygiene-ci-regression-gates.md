# CI Regression Gates

- source canon: `holyshit-mode/github-release-hygiene.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
