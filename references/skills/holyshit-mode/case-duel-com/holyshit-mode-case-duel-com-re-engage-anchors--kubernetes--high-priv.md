# Re-engage anchors — kubernetes / high-priv

- source canon: `holyshit-mode/case-duel-com.md`
- base technique: `holyshit-mode-case-duel-com-re-engage-anchors.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **kubernetes** · auth **high-priv** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- `VITE_BUILD_COMMIT` in the env object (this session: `22aa5245`) = the bundle-hash diff oracle.
- Re-verify first: profile financial fields, socket anon streaming, PaymentIQ test flag. `next --target duel.com` surfaces them.

## Probe adjustment (kubernetes × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
