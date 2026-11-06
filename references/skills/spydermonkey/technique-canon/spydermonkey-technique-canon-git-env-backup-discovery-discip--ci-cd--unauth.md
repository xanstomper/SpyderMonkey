# .git /.env /backup discovery discipline — ci-cd / unauth

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-git-env-backup-discovery-discip.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **ci-cd** · auth **unauth** · chain role **entry**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Distinguish SPA-fallback 200 shells from REAL exposure: require content distinct from the canonical nonexistent-path control (size/content-type delta). Decisive test: control path vs candidate path — identical shell = exhausted, different = the finding.

## Probe adjustment (ci-cd × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
