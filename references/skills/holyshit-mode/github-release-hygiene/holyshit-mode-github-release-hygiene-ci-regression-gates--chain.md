# CI Regression Gates — chain composition

- source canon: `holyshit-mode/github-release-hygiene.md`
- base technique: `holyshit-mode-github-release-hygiene-ci-regression-gates.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
