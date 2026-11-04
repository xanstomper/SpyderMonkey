# Honest-ceiling discipline under operator pressure ("find one") — gcp / low-priv

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-hon.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **gcp** · auth **low-priv** · chain role **pivot**

## Context

- platform: IAM/service-account surface — read-only enumeration
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

The operator repeatedly demanded a true escalation/forge/destructive vector. After
exhausting SSRF (url/base_url params ignored), cloud-metadata/IMDS (no internal proxy),
JWT-forge (opaque DB `session_id`, no signing secret), org-IDOR, admin broken-authz, and
mass-assignment (Turnstile-gated), the correct move was to **state the verified ceiling and
refuse to fabricate** — record the negative in the ledger, don't re-probe in a loop. Real
forges/escalations (key-mint, provisioning, org-admin, BYOK-drain) were all **behind the
auth wall**; without a supplied `xpl_` key/session, they were unreachable by design. Key
lesson: on a hardened dual-surface gateway, the compromisable surface is the misconfigured
internal fleet; the escalation plane is the auth-walled management API — and self-provisioning
credentials to reach it is account fraud, out of scope.

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
