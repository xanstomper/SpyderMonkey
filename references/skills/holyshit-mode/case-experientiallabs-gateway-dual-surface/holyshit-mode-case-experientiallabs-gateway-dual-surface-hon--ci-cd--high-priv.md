# Honest-ceiling discipline under operator pressure ("find one") — ci-cd / high-priv

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-hon.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **ci-cd** · auth **high-priv** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (ci-cd × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
