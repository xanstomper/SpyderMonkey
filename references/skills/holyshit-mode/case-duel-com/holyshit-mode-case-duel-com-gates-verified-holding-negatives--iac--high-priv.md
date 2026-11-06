# Gates verified holding (negatives) — iac / high-priv

- source canon: `holyshit-mode/case-duel-com.md`
- base technique: `holyshit-mode-case-duel-com-gates-verified-holding-negatives.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iac** · auth **high-priv** · chain role **pivot**

## Context

- platform: template/state files are the infrastructure inventory — read-only crown of the exposure
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

`dev/staging/uat` = Cloudflare Access SSO; `capi-automation` S3 = AccessDenied both regions; live-stream S3 = AccessDenied; all sensitive `/api/v2/*` 401 unauth; pvp `/api/v1|v2` = geo-403; pvp arena socket disconnects anon AND user:null-token connects at the namespace gate; `duel.getid.ee` = GetId KYC dashboard login (hypothesis 30).

## Probe adjustment (iac × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
