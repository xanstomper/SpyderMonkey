# Cloud Azure Storage Keys in Config (CLOUD-AZ-02) — gcp / low-priv

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-azure-storage-keys-in-config-.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **gcp** · auth **low-priv** · chain role **pivot**

## Context

- platform: IAM/service-account surface — read-only enumeration
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- class: account keys in app settings/repo
- probe: harvest-class scan of declared configs
- wall: redact on capture — the pattern is the finding, never the key

## Probe adjustment (gcp × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
